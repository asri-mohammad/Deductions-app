from src.datatbase.dbQuery import DBQuery
from src.functionality.constants.resourcePath.insuranceUpdatePath import InsuranceUpdatePath
from src.functionality.decorator.decorator import update_db_invalid_data
from src.functionality.main.insuranceSetting.update.update import Update


class EligibleUpdate(Update):

    ask_msg_file_name = "eligibles.xlsx"
    file_path = InsuranceUpdatePath.eligibles.value

    class DataValidation(Update.DataValidation):
        message = None

        @classmethod
        def validate_data_is_boolean(cls, data):
            """checks if second column of data is all 1 or 0"""

            for data_row in data:
                c2 = data_row[1]
                if not(c2 in {0, 1}):
                    cls.message = " Second column must contain only 1 or 0."
                    return False
            return True

        @classmethod
        def validate(cls, data):
            """validate data before updating DB"""

            if not cls.validate_data_is_boolean(data):
                return False

            return True

    class DBUpdate(Update.DBUpdate):

        @staticmethod
        def data_to_named_data(data):
            """adding names to data that it can be used in sql command placeholders"""

            new_data = []
            for data_row in data:
                data_row_dic = {
                    "e_id": data_row[0],
                    "elg_flag": data_row[1]
                }
                new_data.append(data_row_dic)
            return new_data

        @classmethod
        @update_db_invalid_data
        def update(cls, data):
            """update DB table holding information of those eligible for insurance"""

            named_data = cls.data_to_named_data(data)
            query_string = f"""
                            UPDATE Saman_Insurance_eligible SET is_eligible = :elg_flag 
                            WHERE (employee_id = :e_id AND  is_eligible <> :elg_flag)
                            """
            row_count = DBQuery.bulk_dml_query(query_string, named_data)
            return row_count