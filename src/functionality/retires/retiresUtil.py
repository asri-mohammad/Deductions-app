from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.dateUtil import DateUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class FileSaving:

    # holding the file that is going to be saved
    wb = None

    file_base_name = None  # used as the base for file name
    info_widget_name = None  # to display messages to the user

    @classmethod
    @run_func_disp_err_ret_brk
    def save(cls):
        """let the user saves the output file"""

        info_widget = GUITracker.get(cls.info_widget_name)

        if cls.wb is None:
            GUIUtil.clear_write_text_widget(info_widget, "No file yet, first calculation process.")
            return "break"

        wb_name = cls.FileName.get(cls.file_base_name)

        try:
            wb_is_saved = CommonUtil.save_file(cls.wb, wb_name)

            if wb_is_saved:
                GUIUtil.clear_write_text_widget(info_widget, "File saved.")

        except IOError:
            msg = "Operation Failed. Make sure if your are replacing a file that already exist, the file is not open"
            GUIUtil.clear_write_text_widget(info_widget, msg)

        finally:
            return "break"

    @classmethod
    def set_current_file(cls, wb):
        """let other classes set the file to be saved"""

        cls.wb = wb

    class FileName:

        @staticmethod
        def get(file_base_name):
            """returns file name"""

            file_name = f"{file_base_name}_{DateUtil.date_year_string()}.xlsx"
            return file_name


class FileSelection:

    display_entry_name = None

    @classmethod
    @run_func_disp_err_ret_brk
    def select(cls):
        """opens a file explorer and writes the path of the selected file into entry"""

        path = cls.ask_path()
        cls.display_path(path)
        return "break"

    @staticmethod
    def ask_path():
        """ask the user to select an Excel file and returns its path"""

        file_types = (("Excel files", "*.xlsx"), ("Excel Macro enabled files", "*.xlsm"))
        path = GUIUtil.ask_open_file_name(file_types)
        return path

    @classmethod
    def display_path(cls, path):
        """display the given path in a widget"""

        if path != "":
            display_entry = GUITracker.get(cls.display_entry_name)
            GUIUtil.clear_write_entry_widget(display_entry, path)