from tkinter.messagebox import askyesno, askokcancel, WARNING

from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.main.monthlyData.data.dataStorage import DataStorage
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class BankListDataStorage(DataStorage):
    column_name_data = "bank_list"  # the column where data is stored in it
    column_name_data_sum = "bank_list_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "bank_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_bank_list"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_bank_sum"  # name of the widget to display total sum
    flag_data_type = "national_id"  # it is either employee_id or national_id

    @classmethod
    @run_func_disp_err_ret_brk
    def store(cls):

        msg = """This action could change residues in Database,\n make sure you have chosen the right file.
         \nMaybe a backup of residues  before next step not be a bad idea!!"""
        backup_ok_cancel = askokcancel("Caution", msg, icon=WARNING)
        if not backup_ok_cancel:
            return "break"

        period = MonthlyDataUtil.get_period(output_type="int")

        reordered_data = ExcelDataReading.choose_read_reorder(2, [1, 0])

        if reordered_data is None:  # cancel button
            return "break"
        else:
            data_is_valid = cls.Storage.store(period, reordered_data, cls.flag_data_type, cls.column_name_data)

            if not data_is_valid:
                return "break"

            cls.DataSumStorage.store_column_sum(period, cls.column_name_data, cls.column_name_data_sum)

            data_sum_widget = GUITracker.get(cls.data_sum_widget_name)
            total_sum_widget = GUITracker.get(cls.total_sum_widget_name)
            cls.SumDisplay.update_displayed_sum(period, cls.column_name_data_sum, data_sum_widget)
            cls.SumDisplay.update_displayed_sum(period, cls.column_name_total_sum, total_sum_widget)

            change_residue = cls.ResidueChange.ask()

            if not change_residue:
                return "break"
            else:
                row_count = cls.ResidueReduction.reduce(reordered_data)
                cls.LastEffectivePeriodStorage.store(period)
                MessageUtil.show_message(1, f"Residue updated: {row_count} residues were changed.")
                return "break"

    class ResidueChange:

        @staticmethod
        def get_last_period():
            """returns the last month that the residue got reduced by its bank list """

            query_string = f"""
                            SELECT last_effective_period FROM Saman_Monthly_Data_Config
                            WHERE row_id = 1
                            """

            result = DBQuery.dql_query(query_string)[0][0]
            return result

        @classmethod
        def ask(cls):
            """ask user to reduce the residue by the provided bank list or not"""

            last_month = str(cls.get_last_period())
            question_str = f"Reduce the residue by the given list?\nlast effective month was: {last_month} "
            answer = askyesno(title='confirmation', message=question_str)
            return bool(answer)

    class ResidueReduction:

        @staticmethod
        def remove_none_zero(data):
            """removes None and zero value"""

            new_data = []

            for data_row in data:  # bank list data format is (amount, employee_id)
                amount = data_row[0]
                if (amount != 0) and (amount is not None):
                    new_data.append(data_row)

            return new_data

        @classmethod
        def reduce(cls, data):
            """reduce the residue by the bank list"""

            query_string = f"""
                            UPDATE Saman_Residue SET residue = residue - ? 
                            WHERE employee_id = (SELECT employee_id FROM Saman_Info WHERE national_id = ?);
                            """
            bank_list = cls.remove_none_zero(data)
            row_count = DBQuery.bulk_dml_query(query_string, bank_list)
            return row_count

    class LastEffectivePeriodStorage:

        @staticmethod
        def store(period):
            """store last effective period in DB"""

            query_string = f"""
                            UPDATE Saman_Monthly_Data_Config SET last_effective_period = {period};
                            """
            row_count = DBQuery.dml_query(query_string)
            return row_count