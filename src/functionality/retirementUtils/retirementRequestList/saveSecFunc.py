from tkinter import filedialog as fd

from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.dateUtil import DateUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.commonUtil import  CommonUtil


class SaveSecFunc:
    # holding the file that is going to be saved
    wb = None

    @classmethod
    def set_file(cls, wb):
        """store the given workbook as the file that will be saved if the save button is clicked"""

        cls.wb = wb

    @staticmethod
    def return_file_name():
        """returns the file name"""

        file_name = "ersali_payanKhemdmat_tajmii_" + DateUtil.date_year_string()
        return file_name

    @classmethod
    @run_func_disp_err_ret_brk
    def cmd_save_file(cls):
        """opens a file explorer to choose file location and name and then,
         save the file (if any) and display a saved message """

        text_widget = GUITracker.get("retirement_request_txt_info")

        if cls.wb is None:
            GUIUtil.clear_write_text_widget(text_widget, "No file yet, first calculation process")
            return "break"
        else:
            try:
                file_name = cls.return_file_name()
                is_file_saved = CommonUtil.save_file(cls.wb, file_name)
                if is_file_saved:
                    GUIUtil.clear_write_text_widget(text_widget, "File saved.")
                    return "break"
            except IOError:
                GUIUtil.clear_write_text_widget(text_widget, "Saving Failed :(. Make sure if your are replacing a file"
                                                             "that already exist, the file is not open")