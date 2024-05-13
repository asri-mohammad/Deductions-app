import sqlite3

from src.functionality.constants.resourcePath.dbPath import DBPath
from src.functionality.util.messageUtil import MessageUtil


def run_func_disp_err_ret_brk(func):
    """run a function and display an error message box if sth goes wrong and returns 'break' """

    def extended_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            MessageUtil.show_message(3, f"Something went wrong due to: {str(e)}")
        finally:
            return "break"

    return extended_func


def db_open_run_commit(func):
    """opens a DB connection run func and commit changes
        *** every function that is warped with this function should have cursor as its firs argument
    """

    def extended_func(*args):
        con = None
        cur = None
        try:
            con = sqlite3.connect(DBPath.path.value)
            cur = con.cursor()

            func(cur, *args)

            con.commit()
            return cur.rowcount

        except Exception as err:
            raise err
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    return extended_func


def update_db_invalid_data(func):

    def extended_func(*args, **kwargs):
        try:
            row_count = func(*args, **kwargs)

            if row_count is not None:  # if it is None the function itself handle to display what message
                MessageUtil.show_effected_row(row_count)

            return True

        except sqlite3.IntegrityError:
            MessageUtil.show_message(3, "Invalid data, check the provided data.")
            return False

        except Exception as e:
            raise e

    return extended_func


def singleton(cls):

    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance
