from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.commonUtil import CommonUtil


class MonthlyCalculation:







    @classmethod
    def initialize(cls):
        """all the actions that should be done when the app start up"""
        cls.PeriodSetting.set()
        cls.WorkStatusState.set()
        cls.ResponseSum.set()

    class PeriodSetting:

        @staticmethod
        def set():
            """set the value for the period selection combobox in monthly calculation section"""

            period = DBQuery.dql_query("select period from Saman_Monthly_Calc_config  WHERE row_id = 1;")[0][0]
            period_combobox = GUITracker.get("monthly_calculation_setting_cmb_period")
            period_combobox.set(period)

    class WorkStatusState:

        @staticmethod
        def set():
            """set the work status update checkbox"""

            query_string = "select is_work_status_updated from Saman_Monthly_Calc_Config  WHERE row_id = 1;"
            is_updated = DBQuery.dql_query(query_string)[0][0]
            is_updated_checkbox_var = GUITracker.get("monthly_calculation_chb_var_is_work_status_updated")
            if is_updated == 1:
                is_updated_checkbox_var.set(1)

    class ResponseSum:

        @staticmethod
        def set_response_sum(column_name, lbl_name):
            """read the sum form DB and set the sum value for a response when the app starts"""
            table_name = "Saman_Monthly_Calc_Config"
            lbl = GUITracker.get(lbl_name)
            query_string = f"SELECT {column_name} FROM {table_name} WHERE row_id = 1;"
            column_sum = DBQuery.dql_query(query_string)[0][0]
            column_sum_format = CommonUtil.format_number_comma_separated(column_sum)
            GUIUtil.clear_write_label_widget(lbl, column_sum_format)

        @classmethod
        def set(cls):
            """display the sum for all fields of monthly calculation section"""
            cls.set_response_sum("comptroller_req_sum", "monthly_calc_response_lbl_comptroller_req_sum")
            cls.set_response_sum("comptroller_res_sum", "monthly_calc_response_lbl_comptroller_res_sum")
            cls.set_response_sum("retires_res_sum", "monthly_calc_response_lbl_retires_res_sum")
            cls.set_response_sum("insurance_res_sum", "monthly_calc_response_lbl_insurance_res_sum")
            cls.set_response_sum("overdue_res_sum", "monthly_calc_response_lbl_overdue_res_sum")

