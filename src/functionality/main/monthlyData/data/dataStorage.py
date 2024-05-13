from src.datatbase.dbQuery import DBQuery
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.commonUtil import CommonUtil
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.decorator.decorator import db_open_run_commit
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class DataStorage:

    column_name_data = None  # the column where data is stored in it
    column_name_data_sum = None  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = None  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = None  # name of the widget to display data sum
    total_sum_widget_name = None  # name of the widget to display total sum
    flag_data_type = None  # it is either employee_id or national_id

    @classmethod
    @run_func_disp_err_ret_brk
    def store(cls):

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

            return "break"

    class Storage:

        @staticmethod
        def is_initialized(period):
            """check if already at least data form the given period been stored"""

            query_string = f"""SELECT COUNT(1) FROM Saman_Monthly_Data_Data WHERE period={period} ;"""
            result = DBQuery.dql_query(query_string)[0][0]
            if result == 0:
                return False
            else:
                return True

        @staticmethod
        @db_open_run_commit
        def init_store(cur, column_name, data, period, flag_type):
            """adding rows for the given period and then storing the data """

            query_string = f"""INSERT INTO Saman_Monthly_Data_Data (employee_id, period)
                               SELECT employee_id, {period}  FROM Saman_Info """
            cur.execute(query_string)

            if flag_type == "employee_id":
                query_string = f"""UPDATE Saman_Monthly_Data_Data SET {column_name} = ? 
                                WHERE employee_id = ? AND period = {period};"""
            elif flag_type == "national_id":
                query_string = f"""UPDATE Saman_Monthly_Data_Data SET {column_name} = ? WHERE
                                   employee_id = (SELECT employee_id FROM Saman_Info WHERE national_id = ?) AND period = {period};"""
            cur.executemany(query_string, data)

        @staticmethod
        @db_open_run_commit
        def null_store(cur, column_name, data, period, flag_type):
            """null the column rows for the given period and column name and then storing the data """

            query_string = f"UPDATE Saman_Monthly_Data_Data SET {column_name} = NULL WHERE period = {period}"
            cur.execute(query_string)

            if flag_type == "employee_id":
                query_string = f"""UPDATE Saman_Monthly_Data_Data SET {column_name} = ? 
                                    WHERE employee_id = ? AND period = {period};"""
            elif flag_type == "national_id":
                query_string = f"""UPDATE Saman_Monthly_Data_Data SET {column_name} = ? WHERE
                                       employee_id = (SELECT employee_id FROM Saman_Info WHERE national_id = ?) AND period = {period};"""
            cur.executemany(query_string, data)

        @classmethod
        @update_db_invalid_data
        def store(cls, period, data, flag_data_type, column_name):
            """stores the given data in the given column of DB table where monthly clac records are stored """

            if cls.is_initialized(period):
                return cls.null_store(column_name, data, period, flag_data_type)
            else:
                return cls.init_store(column_name, data, period, flag_data_type)

    class DataSumStorage:

        @staticmethod
        def column_sum(column_name, period):
            """return sum of a column values"""

            query_string = f"SELECT COALESCE(SUM({column_name}),0) from Saman_Monthly_Data_Data WHERE period = {period};"
            column_sum = DBQuery.dql_query(query_string)[0][0]
            return column_sum

        @staticmethod
        def store(period, column_name, column_sum):
            """store the sum in the data summary table for the given period"""

            query_string = f"""INSERT INTO Saman_Monthly_Data_Data_Summary (period, {column_name})
                               VALUES({period}, {column_sum})
                               ON CONFLICT(period) DO UPDATE SET {column_name} = {column_sum} ;
                             """
            row_count = DBQuery.dml_query(query_string)
            return row_count

        @classmethod
        def store_column_sum(cls, period, column_name_to_sum, column_name_to_store):
            """given a period stores the sum of column_name_to_sum in the column_name_to_store"""

            column_sum = cls.column_sum(column_name_to_sum, period)
            cls.store(period, column_name_to_store, column_sum)

    class SumDisplay:
        """
            displaying sum of stored data
        """

        @staticmethod
        def return_column_sum(period, column_name):
            """return the corresponding value for the given column to the provided period"""

            query_string = f"SELECT {column_name} From Saman_Monthly_Data_Data_Summary WHERE period = {period};"
            column_value = DBQuery.dql_query(query_string)[0][0]
            return column_value

        @staticmethod
        def display_sum(lbl_widget, column_sum):
            """display the sum in the given widget"""

            sum_string = CommonUtil.format_number_comma_separated(column_sum)
            GUIUtil.clear_write_label_widget(lbl_widget, sum_string)

        @classmethod
        def update_displayed_sum(cls, period, column, widget):
            """given period and column names where sum and total sum is stored,
               each value will be displayed in the provided widgets
            """

            column_sum = cls.return_column_sum(period, column)
            cls.display_sum(widget, column_sum)
