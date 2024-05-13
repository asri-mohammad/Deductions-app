from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil


class Backup:

    @classmethod
    def initialize(cls):
        """all the actions that should be done when the app start up"""
        cls.StorageDirectory.display_directory()

    class StorageDirectory:

        @staticmethod
        def retrieve_directory():
            """retrieve directory from DB"""

            query_string = f"""
                            SELECT backup_path FROM backup_config WHERE row_id = 1;
                            """
            directory = DBQuery.dql_query(query_string)[0][0]
            return directory

        @staticmethod
        def display(directory):
            """display the directory in the entry"""

            entry_widget = GUITracker.get("backup_ent_backup_dir")
            GUIUtil.clear_write_entry_widget(entry_widget, directory)

        @classmethod
        def display_directory(cls):
            """fetch directory from db and display it"""

            directory = cls.retrieve_directory()
            cls.display(directory)