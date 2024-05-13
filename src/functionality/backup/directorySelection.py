from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class DirectorySelection:

    @classmethod
    @run_func_disp_err_ret_brk
    def cmd_select_directory(cls):
        """let the user select a directory and then store and display the selected directory path"""

        dir_path = cls.Selection.select()

        if dir_path == "":  # cancel button
            return "break"

        entry_widget = GUITracker.get("backup_ent_backup_dir")
        cls.Display.display(entry_widget, dir_path)
        cls.Storage.store(dir_path)
        return "break"

    class Selection:

        @staticmethod
        def select():
            """opens a file explorer and let user select a directory, return None in case user cancels the operation"""

            path = GUIUtil.ask_directory()
            return path

    class Display:

        @staticmethod
        def display(ent_widget, dir_path):
            """display the given path in the given entry widget"""

            GUIUtil.clear_write_entry_widget(ent_widget, dir_path)

    class Storage:

        @staticmethod
        def store(dir_path):
            """stores the given path in the DB"""

            query_string = f"""
                            UPDATE backup_config set backup_path = "{dir_path}" WHERE row_id = 1;
                            """
            DBQuery.dml_query(query_string)

