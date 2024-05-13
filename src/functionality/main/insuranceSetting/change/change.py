from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.excelUtil.excelFileOpening import ExcelFileOpening


class Change:

    excel_file_path = None

    @classmethod
    @run_func_disp_err_ret_brk
    def open(cls):
        """Opens an Excel file to let user update DB through the file"""

        ExcelFileOpening.open(cls.excel_file_path)