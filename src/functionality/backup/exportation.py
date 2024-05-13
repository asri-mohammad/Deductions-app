import time
import os
import shutil
import pathlib

from src.functionality.constants.resourcePath.dbPath import DBPath
from src.functionality.util.dateUtil import DateUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.gui.customWidget.customDialogBox import CustomDialogBox
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.messageUtil import MessageUtil


class Exportation:

    @classmethod
    @run_func_disp_err_ret_brk
    def cmd_export(cls):
        """let the user save a copy of the DB in a selected directory"""

        directory = cls.Directory.get()

        if not pathlib.Path(directory).is_dir():
            MessageUtil.show_message(2, "Please provide a valid directory to store the backup file.")
            return "break"

        file_name = cls.FileName.select()

        if file_name is None:  # cancel button
            return "break"

        cls.Save.save(directory, file_name)
        MessageUtil.show_message(1, "File saved.")
        return "break"

    class Directory:

        @staticmethod
        def get():
            """get the directory path selected by user from an entry widget"""

            entry_widget = GUITracker.get("backup_ent_backup_dir")
            directory = entry_widget.get()
            return directory

    class FileName:

        @staticmethod
        def get_date():
            """return date in format ymd for example 14021022"""

            current_system_date = DateUtil.today()
            date = current_system_date.replace("/", "")
            return date

        @staticmethod
        def get_time():
            """returns time in format hs for example 1457"""

            current_system_time = time.strftime('%H%M')
            return current_system_time

        @classmethod
        def select(cls):
            """pop up a dialog box to let the user confirm or select a date and a time"""

            current_time = cls.get_time()
            current_date = cls.get_date()

            datetime = CustomDialogBox.askstring("Data Confirmation", "Date : ", "Time : ", current_date, current_time)

            if datetime is None:  # cancel button
                return None

            the_date = datetime[0]
            the_time = datetime[1]
            file_name = f"{the_date}-{the_time}.db"
            return file_name

    class Save:

        @staticmethod
        def save(dir_path, file_name):
            """copy the DB as the given file name in the given directory path"""

            shutil.copy(DBPath.path.value, os.path.join(dir_path, file_name))


