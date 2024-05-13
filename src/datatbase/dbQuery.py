import sqlite3

from src.functionality.constants.resourcePath.dbPath import DBPath


class DBQuery:

    @staticmethod
    def dql_query(query_string):
        """data query language type of queries"""
        con = None
        cur = None
        try:
            con = sqlite3.connect(DBPath.path.value)
            cur = con.cursor()
            result = cur.execute(query_string).fetchall()
            return result
        except Exception as err:
            raise err
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    @staticmethod
    def dml_query(query_string):
        """data Manipulation  language type of queries"""
        con = None
        cur = None
        try:
            con = sqlite3.connect(DBPath.path.value)
            cur = con.cursor()
            cur.execute(query_string)
            con.commit()
            return cur.rowcount
        except Exception as err:
            raise err
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    @staticmethod
    def bulk_dml_query(query_string, data):
        """data Manipulation  language type of queries in bulk"""
        con = None
        cur = None
        try:
            con = sqlite3.connect(DBPath.path.value)
            cur = con.cursor()
            cur.executemany(query_string, data)
            con.commit()
            return cur.rowcount
        except Exception as err:
            raise err
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    @staticmethod
    def script_query(script):
        """data Manipulation  language type of queries in bulk"""
        con = None
        cur = None
        try:
            con = sqlite3.connect(DBPath.path.value)
            cur = con.cursor()
            cur.executescript(script)
            con.commit()
            return cur.rowcount
        except Exception as err:
            raise err
        finally:
            if cur:
                cur.close()
            if con:
                con.close()