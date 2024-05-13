from tkinter import simpledialog

from src.datatbase.dbQuery import DBQuery
from src.functionality.util.dateUtil import DateUtil
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.util.commonUtil import CommonUtil


class GeneralStatusUpdate:

    @classmethod
    @run_func_disp_err_ret_brk
    def cmd_batch_update(cls):
        """reads form a file and update and update DB accordingly"""

        confirmed_date = cls.DateConfirmation.confirm()

        if confirmed_date is None:  # cancel button
            return "break"

        data = ExcelDataReading.choose_read(2)

        if data is None:
            return "break"

        reordered_data = CommonUtil.reorder_column(data, [1, 0])

        cls.DBUpdate.update(reordered_data, confirmed_date)
        return "break"

    class DateConfirmation:

        @staticmethod
        def confirm():
            """return a string representing date and None if cancel button is clicked on"""

            current_system_date = DateUtil.today()
            title = "Data confirmation"
            prompt = "Please enter the date:"
            confirmed_date = simpledialog.askstring(title=title, prompt=prompt, initialvalue=current_system_date)
            return confirmed_date

    class DBUpdate:

        @staticmethod
        @update_db_invalid_data
        def update(data, date):
            """update values of the selected column in the given table name based on provided data using employee_id"""

            query_string = f"""UPDATE Saman_General_Status
                                SET general_status = ?, registration_date = "{date}" WHERE employee_id = ?;"""
            row_count = DBQuery.bulk_dml_query(query_string, data)
            return row_count