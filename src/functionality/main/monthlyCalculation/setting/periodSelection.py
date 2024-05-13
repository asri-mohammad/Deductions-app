from src.datatbase.dbQuery import DBQuery
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil


class PeriodSelection:

    @staticmethod
    def write_to_db(period):
        """gets a period as a string and set the active period in database accordingly"""
        # TODO: changing period from text to integer in db and code
        query_string = f'UPDATE Saman_Monthly_Calc_config SET period = "{period}" WHERE row_id = 1;'
        row_count = DBQuery.dml_query(query_string)
        if row_count != 1:
            raise Exception("Sth when wrong went writing monthly calculation period into DB. :(")

    @staticmethod
    @run_func_disp_err_ret_brk
    def store():
        """set the selected period into DB"""

        period = MonthlyCalcUtil.get_period()
        PeriodSelection.write_to_db(period)
