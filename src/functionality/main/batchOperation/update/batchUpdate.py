from src.datatbase.dbQuery import DBQuery
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
from src.functionality.util.commonUtil import CommonUtil


class BatchUpdate:

    """
        a general parent class
    """

    table_name = None
    column_name = None

    @classmethod
    @run_func_disp_err_ret_brk
    def cmd_batch_update(cls):
        """reads form a file and updates DB accordingly"""

        data = ExcelDataReading.choose_read(2)

        if data is None:
            return "break"

        reordered_data = CommonUtil.reorder_column(data, [1, 0])

        cls.DBUpdate.update(cls.table_name, cls.column_name, reordered_data)
        return "break"

    class DBUpdate:

        @staticmethod
        @update_db_invalid_data
        def update(table_name, column_name, data):
            """update values of the selected column in the given table name based on provided data using employee_id"""

            query_string = f"""UPDATE {table_name}
                                SET {column_name} = ? WHERE employee_id = ?;"""
            row_count = DBQuery.bulk_dml_query(query_string, data)
            return row_count