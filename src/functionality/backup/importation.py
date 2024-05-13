import shutil

from src.functionality.constants.resourcePath.dbPath import DBPath
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.startup.startup import Startup
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class Importation:

    @classmethod
    @run_func_disp_err_ret_brk
    def cmd_import(cls):
        """let user select a new DB and replace the current DB"""

        new_db_path = cls.Selection.select()

        if new_db_path == "":  # cancel button
            return "break"

        cls.Replacement.replace(new_db_path)
        cls.AppRefresh.refresh()
        MessageUtil.show_message(1, "Import done.")
        return "break"

    class Selection:

        @staticmethod
        def select():
            """let user select a DB file"""

            path = GUIUtil.ask_open_file_name(document_type="sqlite_db")
            return path

    class Replacement:

        @staticmethod
        def replace(file_path):
            """replace the database with new one that is selected"""

            shutil.copy(file_path, DBPath.path.value)

    class AppRefresh:

        @staticmethod
        def refresh():
            """sync the app with newly provide DB"""

            Startup.initialize()