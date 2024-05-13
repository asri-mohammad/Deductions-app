from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.periodUtil import PeriodUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil


class BankList:

    is_employees_provided = False
    is_retires_provided = False
    is_insurance_provided = False

    is_employees_selected = False
    is_retires_selected = False
    is_insurance_selected = False

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """ command that generate the bank list if other criteria are right"""

        cls.DataProvision.is_provided()
        cls.ItemSelection.is_selected()

        if (cls.is_employees_selected or cls.is_retires_selected or cls.is_insurance_selected) is False:  # no selection
            MessageUtil.show_message(1,  "At leas one item must be selected.")
            return "break"

        deselect_list = cls.ItemDeselection.get_item()
        if deselect_list:
            MessageUtil.show_message(1, f' please deselect:\n {", ".join(deselect_list)}')
            return "break"

        raw_data = cls.DataRetrieval.retrieve()
        processed_data = cls.DataProcess.process(raw_data)
        wb = cls.ExcelFile.generate(processed_data)
        cls.FileFormat.format(wb)
        wb_name = cls.FileName.get()
        CommonUtil.save_file(wb, wb_name)
        return "break"

    class DataProvision:

        @staticmethod
        def get_column_sum(column_name):
            """ returns the sum of the given column form DB table Saman_Monthly_Calc_Config"""

            query_string = f"SELECT {column_name} FROM Saman_Monthly_Calc_Config where row_id = 1;"
            column_sum = DBQuery.dql_query(query_string)[0][0]
            return column_sum

        @classmethod
        def is_provided(cls):
            """set the variables indicating if responses (comptroller, retires, insurance) was set or not"""

            BankList.is_employees_provided = True if cls.get_column_sum("comptroller_res_sum") > 0 else False
            BankList.is_retires_provided = True if cls.get_column_sum("retires_res_sum") > 0 else False
            BankList.is_insurance_provided = True if cls.get_column_sum("insurance_res_sum") > 0 else False

    class ItemSelection:

        @classmethod
        def is_selected(cls):
            """set the variables indicating if checkboxes (comptroller, retires, insurance) are checked or not"""

            employees_chb_var = GUITracker.get("monthly_calc_bank_list_chb_var_employees").get()
            retires_chb_var = GUITracker.get("monthly_calc_bank_list_chb_var_retires").get()
            insurance_chb_var = GUITracker.get("monthly_calc_bank_list_chb_var_insurance").get()
            BankList.is_employees_selected = True if employees_chb_var == 1 else False
            BankList.is_retires_selected = True if retires_chb_var == 1 else False
            BankList.is_insurance_selected = True if insurance_chb_var == 1 else False

    class ItemDeselection:

        @staticmethod
        def get_item():
            """provide a list of items that are selected but the corresponding responses are not provided"""

            deselect_list = []
            
            if (BankList.is_employees_selected is True) and (BankList.is_employees_provided is False):
                deselect_list.append("employees")
            if (BankList.is_retires_selected is True) and (BankList.is_retires_provided is False):
                deselect_list.append("retires")
            if (BankList.is_insurance_selected is True) and (BankList.is_insurance_provided is False):
                deselect_list.append("insurance")
                
            return deselect_list

    class DataRetrieval:

        @classmethod
        def get_selected_item(cls):
            """return a list of DB column names corresponding to checkboxes that are checked"""

            column_name_list = []
            if BankList.is_employees_selected:
                column_name_list.append("comptroller_res")
            if BankList.is_retires_selected:
                column_name_list.append("retires_res")
            if BankList.is_insurance_selected:
                column_name_list.append("insurance_res")
            return column_name_list

        @classmethod
        def retrieve(cls):
            """returns the non-zero data for selected items(employees, retires, insurance)"""

            column_name_list = cls.get_selected_item()
            sum_string = " + ".join(column_name_list)
            query_string = f"""SELECT branch_id, customer_id, national_id, first_name, last_name, ({sum_string})
                                    FROM Saman_Info
                                    INNER JOIN  Saman_Monthly_Calc_Data ON Saman_Info.employee_id = Saman_Monthly_Calc_Data.employee_id
                                    WHERE ({sum_string}) != 0;"""
            data = DBQuery.dql_query(query_string)
            return data

    class DataProcess:

        @staticmethod
        def get_generator(data):
            """generator function for the given data, it adds two more columns to data"""

            period = PeriodUtil.previous_month_int(MonthlyCalcUtil.get_period(output_type="int"))

            for idx, row in enumerate(data):
                row = list(row)
                row.insert(0, idx + 1)
                row.insert(6, period)
                yield row

        @classmethod
        def process(cls, data):
            """returns a generator of fully processed, ready to write in file, data"""

            return cls.get_generator(data)

    class ExcelFile:

        @staticmethod
        def write_header(ws):
            """write the header row of the file"""

            header_list = ["ردیف", "کد شعبه", "کد مشتری", "کد ملی", "نام", "نام خانوادگی", "دوره", "مبلغ"]
            OpenpyxlUtil.write_header(ws, header_list)

        @staticmethod
        def write_total_sum(ws):
            """adds a total sum row at the end of the data area of the sheet"""
            
            row_count = ws.max_row
            ws[f'G{row_count + 2}'] = "جمع کل"
            ws[f'H{row_count + 2}'] = f"=SUM(H2:H{row_count})"

        @classmethod
        def generate(cls, data):
            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws)
            OpenpyxlUtil.write_data(ws, data)
            cls.write_total_sum(ws)
            return wb
            
    class FileFormat:
        @staticmethod
        def format(wb):
            """formatting the given workbook"""
            
            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [("c", "H", 18)])
            OpenpyxlUtil.format_column_comma_separated(ws, ["H"], starting_row=2)
            
    class FileName:
        
        @staticmethod
        def get():
            """create a name for bank list file based on items that are selected"""

            period = PeriodUtil.previous_month_str(MonthlyCalcUtil.get_period())

            if (BankList.is_employees_selected and BankList.is_retires_selected and BankList.is_insurance_selected) is True:
                return f"{period}_saman_ersali_bank_all"
            else:
                item_name_list = []
                if BankList.is_employees_selected:
                    item_name_list.append("employees")
                if BankList.is_retires_selected:
                    item_name_list.append("retires")
                if BankList.is_insurance_selected:
                    item_name_list.append("insurance")
                return f"{period}_saman_ersali_bank_{'_'.join(item_name_list)}"
            