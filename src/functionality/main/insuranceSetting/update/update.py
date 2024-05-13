from tkinter.messagebox import askyesno

from src.functionality.util.messageUtil import MessageUtil
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class Update:

    ask_msg_file_name = None
    file_path = None

    @classmethod
    @run_func_disp_err_ret_brk
    def update(cls):
        """updating DB"""

        is_file_saved = cls.ExcelSave.ask(cls.ask_msg_file_name)

        if not is_file_saved:
            MessageUtil.show_message(1, "Then save the file first and retry.")
            return "break"

        data = ExcelDataReading.read(cls.file_path, 2)

        is_data_valid = cls.DataValidation.validate(data)

        if not is_data_valid:
            message = cls.DataValidation.message
            MessageUtil.show_message(3, f"Operation Failed, due to: \n {message}")
            return "break"

        cls.DBUpdate.update(data)
        return "break"

    class ExcelSave:

        @staticmethod
        def ask(file_name):
            """asking user if the file has been saved or not"""

            answer = askyesno(title='Confirmation', message=f"Did you save the Excel file {file_name}?")
            return bool(answer)

    class DataValidation:

        message = None

        # add each validation function here

        @classmethod
        def validate(cls, data):
            """validate data before updating DB"""

            # test each function here

            return True

    class DBUpdate:

        @classmethod
        def update(cls, data):
            """update DB with provided data"""

            pass