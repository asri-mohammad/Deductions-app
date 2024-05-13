import shutil
import os

from src.functionality.util.guiUtil import GUIUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.constants.constants import not_allowed_to_save_dir
from src.functionality.util.messageUtil import MessageUtil


class Sample:

    @staticmethod
    @run_func_disp_err_ret_brk
    def cmd_sample(src_file_path, des_file_name=None, file_type="excel"):
        """Opens a file explorer so user select a directory to save given Excel file
           if file name is not provided, the original file name will be used
        """

        if des_file_name is not None:
            file_name = des_file_name
        else:
            file_name = CommonUtil.get_file_name_from_path(src_file_path)

        directory_path = GUIUtil.ask_save_file_name(file_name, file_type=file_type)

        if directory_path == "":  # user clicked on cancel button
            return "break"
        elif CommonUtil.is_in_sub_dir(not_allowed_to_save_dir, directory_path):
            MessageUtil.show_message(2, "You are not allowed to save file in this location.")
            return "break"
        else:
            shutil.copy(src_file_path, directory_path)
            return "break"