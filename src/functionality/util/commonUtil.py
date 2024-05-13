import os
from pathlib import Path

from src.functionality.util.guiUtil import GUIUtil
from src.functionality.constants.constants import not_allowed_to_save_dir
from src.functionality.util.messageUtil import MessageUtil


class CommonUtil:
    @staticmethod
    def check_file_exist(path):
        """ check if the file for the give path exits and returns true or false"""
        return os.path.isfile(path)

    @staticmethod
    def format_number_comma_separated(number):
        """change number  1000 to 1,000"""
        return "{:,}".format(int(number))

    @staticmethod
    def persian_to_arabic(s):
        """changes persian letters to arabic"""
        s = s.replace("ی", "ي")
        s = s.replace("ک", "ك")
        return s

    @staticmethod
    def arabic_to_persian(s):
        """changes arabic letters to persian"""
        s = s.replace("ي", "ی")
        s = s.replace("ك", "ک")
        return s

    @staticmethod
    def pop_up_err_message(e):
        """shows the error message in an error message box"""
        MessageUtil.show_message(3, e.message)

    @staticmethod
    def is_in_sub_dir(main_dir, potential_sub_dir):
        """given a directory and a directory/file_path check if is equal to/in the given directory or its subdirectories """

        return Path(main_dir) in [Path(potential_sub_dir)] + [p for p in Path(potential_sub_dir).parents]

    @staticmethod
    def save_file(file, file_name, ask_type="file_name", file_type="excel"):
        """
            ask the user for a directory and then save the file with the given file_name in the chosen directory
            returns True if file is saved and False in other cases
        """

        full_path = ""

        if ask_type == "directory":
            directory_path = GUIUtil.ask_directory()
            full_path = os.path.join(directory_path, file_name)
        elif ask_type == "file_name":
            full_path = GUIUtil.ask_save_file_name(file_name, file_type=file_type)

        if full_path == "":  # if user click on cancel button
            return False
        elif CommonUtil.is_in_sub_dir(not_allowed_to_save_dir, full_path):
            MessageUtil.show_message(2, "You are not allowed to save file in this location.")
            return False
        else:
            file.save(full_path)
            return True

    @staticmethod
    def reorder_column(matrix, column_order):
        """given a matrix-like variable reorders the variable column, column_order index starting from 0"""

        new_matrix = []
        for row in matrix:
            new_row = [None for i in range(0, len(matrix[0]))]
            for i, c in enumerate(row):
                new_row[column_order[i]] = c
            new_matrix.append(new_row)
        return new_matrix

    @staticmethod
    def get_file_name_from_path(file_path):
        """returns file name.extension from file path"""

        file_name = os.path.basename(file_path)
        return file_name


