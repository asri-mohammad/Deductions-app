from src.datatbase.dbQuery import DBQuery
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil


class WorkStatusState:

    @classmethod
    @run_func_disp_err_ret_brk
    def update(cls):

        period = MonthlyCalcUtil.get_period()

        if period == "":  # no period is selected in combobox
            MessageUtil.show_message(2, "Please first select a period.")
            return "break"

        cls.store(MonthlyCalcUtil.work_status_update_state())
        return "break"

    @staticmethod
    def store(binary_value):
        """set the is_work_status_updated value in db to the binary_value for the given period"""

        query_string = f'update Saman_Monthly_Calc_Config set is_work_status_updated = {binary_value} where row_id = 1;'
        DBQuery.dml_query(query_string)
