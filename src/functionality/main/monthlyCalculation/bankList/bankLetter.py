import random
from docx import Document

from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.customWidget.customDialogBox import CustomDialogBox
from src.functionality.constants.constants import number_to_persian_month_dict
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.main.monthlyCalculation.bankList.bankLetterUtils.wordMaker import WordMaker
from src.functionality.constants.resourcePath.samplePath import SamplePath
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.dateUtil import DateUtil
from src.functionality.util.periodUtil import PeriodUtil
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil

"""
road map:
1 find the sum that should be written in the letter based on selected items
2 confirm date and total amount with user
3 make word document ready and save it in the user selected directory
"""


class BankLetter:

    is_employees_selected = False
    is_retires_selected = False
    is_insurance_selected = False

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """generate bank letter and store it in user selected directory"""

        initial_amount = CommonUtil.format_number_comma_separated(cls.LetterAmount.get())
        initial_date = DateUtil.today()

        final_date_amount = cls.Confirmation.confirm(initial_date, initial_amount)

        if final_date_amount is None:  # user clicked on cancel button when is prompted to confirm date and amount
            return "break"

        final_date, final_amount = final_date_amount

        final_wd_doc = cls.Letter.generate(final_date, final_amount)
        file_name = cls.LetterName.get_name()
        CommonUtil.save_file(final_wd_doc, file_name, file_type="word")
        return "break"

    class ItemSelection:

        @staticmethod
        def is_selected():
            """set the variables indicating if checkboxes (comptroller, retires, insurance) are selected or not"""

            employees_chb_var = GUITracker.get("monthly_calc_bank_list_chb_var_employees").get()
            retires_chb_var = GUITracker.get("monthly_calc_bank_list_chb_var_retires").get()
            insurance_chb_var = GUITracker.get("monthly_calc_bank_list_chb_var_insurance").get()
            BankLetter.is_employees_selected = True if employees_chb_var == 1 else False
            BankLetter.is_retires_selected = True if retires_chb_var == 1 else False
            BankLetter.is_insurance_selected = True if insurance_chb_var == 1 else False

    class LetterAmount:
        @staticmethod
        def get_column_sum(column_name):
            """ returns the sum of the given column form DB table Saman_Monthly_Calc_Config"""

            query_string = f"SELECT {column_name} FROM Saman_Monthly_Calc_Config where row_id = 1;"
            column_sum = DBQuery.dql_query(query_string)[0][0]
            return column_sum

        @classmethod
        def get(cls):
            """return the sum of value that must be written in the letter based on the selected items"""

            amount = 0

            BankLetter.ItemSelection.is_selected()

            if BankLetter.is_employees_selected:
                column_sum = cls.get_column_sum("comptroller_res_sum")
                amount += column_sum
            if BankLetter.is_retires_selected:
                column_sum = cls.get_column_sum("retires_res_sum")
                amount += column_sum
            if BankLetter.is_insurance_selected:
                column_sum = cls.get_column_sum("insurance_res_sum")
                amount += column_sum

            return amount

    class Confirmation:

        @staticmethod
        def confirm(date, amount):
            """shows a dialog to user to confirm data and total value to be written in the letter, also
                user can change the values too
                returns a list {value 1 , value 2 }
                """

            date_amount = CustomDialogBox.askstring("Bank letter", "letter's date:", "amount:", date, amount)
            return date_amount

    class LetterNumber:
        @staticmethod
        def generate():
            """returns a random number representing letter number"""

            random_part = str(random.randrange(1, 99999))
            return "11/12/3/" + random_part
    
    class Letter:

        @staticmethod
        def get_placeholder_value(date, amount):
            """return a dictionary containing corresponding values to word template placeholders
            <date>, <letter_num>, <year>, <month>, <amount>"""

            date = date
            letter_num = BankLetter.LetterNumber.generate()
            period = PeriodUtil.previous_month_str(MonthlyCalcUtil.get_period())
            year = period[0:4]
            month_num_str = str(int(period[4:6]))
            month = number_to_persian_month_dict[month_num_str]
            amount = amount

            placeholder_value_dict = {
                "date": date,
                "letter_num": letter_num,
                "year": year,
                "month": month,
                "amount": amount
            }

            return placeholder_value_dict
        
        @classmethod
        def generate(cls, date, amount):
            """generate the bank letter word document"""

            place_holder_values = cls.get_placeholder_value(date, amount)
            template_wd_doc = Document(SamplePath.bank_letter.value)
            final_wd_doc = WordMaker.make_word_doc(template_wd_doc, place_holder_values)
            return final_wd_doc

    class LetterName:
        @staticmethod
        def get_name():
            """create a name for bank list file based on items that are selected"""

            period = PeriodUtil.previous_month_str(MonthlyCalcUtil.get_period())

            if (BankLetter.is_employees_selected and BankLetter.is_retires_selected and BankLetter.is_insurance_selected) is True:
                return f"{period}_saman_ersali_bank_all"
            elif (BankLetter.is_employees_selected or BankLetter.is_retires_selected or BankLetter.is_insurance_selected) is False:
                return f"{period}_saman_ersali_bank_none"
            else:
                item_name_list = []
                if BankLetter.is_employees_selected:
                    item_name_list.append("employees")
                if BankLetter.is_retires_selected:
                    item_name_list.append("retires")
                if BankLetter.is_insurance_selected:
                    item_name_list.append("insurance")
                return f"{period}_saman_ersali_bank_{'_'.join(item_name_list)}"
        