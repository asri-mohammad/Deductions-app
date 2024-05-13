from src.datatbase.dbQuery import DBQuery


class DBUtil:

    @staticmethod
    def retrieve(query_string):
        """query the given string and returns result"""

        result = DBQuery.dql_query(query_string)
        return result

    @staticmethod
    def get_column_sum(table_name, column_name):
        """return sum of a column values"""

        query_string = f"SELECT SUM({column_name}) from {table_name};"
        column_sum = DBQuery.dql_query(query_string)[0][0]
        return column_sum


class DataRetrieval:

    query_string = None

    @classmethod
    def retrieve(cls):

        return DBUtil.retrieve(cls.query_string)