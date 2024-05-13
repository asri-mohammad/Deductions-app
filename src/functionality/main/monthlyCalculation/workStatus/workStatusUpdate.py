from src.datatbase.dbQuery import DBQuery
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading


class WorkStatusUpdate:

    @classmethod
    @run_func_disp_err_ret_brk
    def update(cls):

        reordered_data = ExcelDataReading.choose_read_reorder(2, [1, 0])

        if reordered_data is None:
            return "break"

        cls.store(reordered_data)
        return "break"

    @staticmethod
    @update_db_invalid_data
    def store(data):
        query_string = "update Saman_Work_Status set work_status_id = ? where employee_id = ?;"
        row_count = DBQuery.bulk_dml_query(query_string, data)
        return row_count
