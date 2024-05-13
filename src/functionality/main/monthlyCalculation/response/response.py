from src.gui.guiTracking.guiTracker import GUITracker
from src.datatbase.dbQuery import DBQuery
from src.datatbase.dbUtil import DBUtil
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.decorator.decorator import db_open_run_commit
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading


class Response:

    data_table_name = "Saman_Monthly_Calc_Data"  # table where monthly cal data is stored in
    data_column_name = None  # the column where data must be stored in for monthly calculation
    config_table_name = "Saman_Monthly_Calc_Config"  # table where general config and info for monthly calculation is stored in
    config_column_name = None  # the column where the following config must be stored in
    sum_lbl_name = None  # the name of the label widget to display the sum of the provided column

    @classmethod
    @run_func_disp_err_ret_brk
    def set(cls):
        """command to set the response in database and display the sum in the label widget"""

        reordered_data = ExcelDataReading.choose_read_reorder(2, [1, 0])

        if reordered_data is None:  # cancel button
            return 'break'

        # storing the provided data
        cls.DataStorage.store(cls.data_table_name, cls.data_column_name, reordered_data)

        # calculate sum and store it
        data_sum = DBUtil.get_column_sum(cls.data_table_name, cls.data_column_name)
        cls.DataSumStorage.store(cls.config_table_name, cls.config_column_name, data_sum)

        # displaying sum
        disp_sum_widget = GUITracker.get(cls.sum_lbl_name)
        cls.DataSumDisplay.display(disp_sum_widget, data_sum)

    class DataStorage:
        @staticmethod
        @update_db_invalid_data
        @db_open_run_commit
        def store(cur, table_name, column_name, data):
            """update DB according to the given data based on employee_id"""

            query_string = f"UPDATE {table_name} SET {column_name} = 0"
            cur.execute(query_string)

            query_string = f"UPDATE {table_name} set {column_name} = ? where employee_id = ?;"
            cur.executemany(query_string, data)

    class DataSumStorage:
        @staticmethod
        def store(table_name, column_name, column_sum):
            """store the sum in the database"""

            query_string = f"UPDATE {table_name} set {column_name} = {column_sum} where row_id = 1;"
            row_count = DBQuery.dml_query(query_string)
            return row_count

    class DataSumDisplay:
        @staticmethod
        def display(lbl_widget, column_sum):
            """display the sum in the given widget"""

            sum_string = CommonUtil.format_number_comma_separated(column_sum)
            GUIUtil.clear_write_label_widget(lbl_widget, sum_string)