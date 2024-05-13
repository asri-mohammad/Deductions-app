from src.datatbase.dbQuery import DBQuery
from src.functionality.constants.resourcePath.insuranceUpdatePath import InsuranceUpdatePath
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.main.insuranceSetting.update.update import Update


class ReasonUpdate(Update):

    ask_msg_file_name = "reasons.xlsx"
    file_path = InsuranceUpdatePath.reasons.value

    class DataValidation(Update.DataValidation):
        message = None

        @classmethod
        def validate_data_not_be_empty(cls, data):
            """checks at least there is one row of data"""

            if not data:
                cls.message = "At least there must be one row of data"
                return False
            return True

        @classmethod
        def validate_code_all_integer(cls, data):
            """checks if first column of data is all integer"""

            for data_row in data:
                c1 = data_row[0]
                if not isinstance(c1, int):
                    cls.message = " First column, code, must be all an integer number"
                    return False
            return True

        @classmethod
        def validate_no_duplicate(cls, data):
            """checks the first column for duplicate values"""

            code_list = [data_row[0] for data_row in data]
            if len(code_list) != len(set(code_list)):
                cls.message = "Duplicate values in first column"
                return False
            return True

        @classmethod
        def validate(cls, data):
            """validate data before updating DB"""

            if not cls.validate_data_not_be_empty(data):
                return False
            if not cls.validate_code_all_integer(data):
                return False
            if not cls.validate_no_duplicate(data):
                return False
            return True

    class DBUpdate(Update.DBUpdate):

        @staticmethod
        def clear_table(table_name):
            """delete all rows of data for the given table"""

            query_string = f"""DELETE from {table_name}"""
            row_count = DBQuery.dml_query(query_string)
            return row_count

        @staticmethod
        def insert_data(table_name, data):
            """insert datat into table"""

            query_string = f"""
                            INSERT INTO {table_name} (code, reason) VALUES (?, ?);
                            """
            row_count = DBQuery.bulk_dml_query(query_string, data)
            return row_count

        @classmethod
        @update_db_invalid_data
        def update(cls, data):
            """refresh DB table holding insurance code and reasons"""

            table_name = "Insurance_Reason"
            cls.clear_table(table_name)
            row_count = cls.insert_data(table_name, data)
            MessageUtil.show_message(1, f"Updated. New reasons table has {row_count} rows now.")
            return None

