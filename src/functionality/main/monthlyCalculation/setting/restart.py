from src.gui.guiTracking.guiTracker import GUITracker
from src.datatbase.dbQuery import DBQuery
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class Restart:

    @classmethod
    @run_func_disp_err_ret_brk
    def reset(cls):
        """reset GUI and DB to a clean start state"""

        cls.GUIRestart.reset()
        cls.DBRestart.reset()

    class GUIRestart:

        @staticmethod
        def reset_label():
            """reset labels in GUI"""

            labels_list = [
                GUITracker.get("monthly_calc_response_lbl_comptroller_req_sum"),
                GUITracker.get("monthly_calc_response_lbl_comptroller_res_sum"),
                GUITracker.get("monthly_calc_response_lbl_retires_res_sum"),
                GUITracker.get("monthly_calc_response_lbl_insurance_res_sum"),
                GUITracker.get("monthly_calc_response_lbl_overdue_res_sum")
            ]

            for label in labels_list:
                GUIUtil.clear_write_label_widget(label, "0")

        @staticmethod
        def reset_checkbutton():
            """resets checkbuttons in GUI"""

            checkbutton_list = [
                GUITracker.get("monthly_calculation_chb_var_is_work_status_updated"),

                GUITracker.get("monthly_calc_bank_list_chb_var_employees"),
                GUITracker.get("monthly_calc_bank_list_chb_var_retires"),
                GUITracker.get("monthly_calc_bank_list_chb_var_insurance")
            ]

            for chb in checkbutton_list:
                chb.set(False)

        @classmethod
        def reset(cls):
            """handel GUI part of reset"""

            cls.reset_label()
            cls.reset_checkbutton()

    class DBRestart:

        @staticmethod
        def reset_calc_data():
            """resets table which holds monthly calc data for calculation"""

            query_string = f"""
                            UPDATE Saman_Monthly_Calc_Data  SET 
                            comptroller_req = 0,
                            comptroller_res = 0,
                            insurance_res = 0,
                            overdue_res = 0,
                            retires_res = 0 
                            """
            return query_string

        @staticmethod
        def reset_total_sums():
            """reset records holding total sum"""

            query_string = f"""
                            UPDATE Saman_Monthly_Calc_Config  SET 
                            comptroller_req_sum = 0,
                            comptroller_res_sum = 0,
                            insurance_res_sum = 0,
                            overdue_res_sum = 0,
                            retires_res_sum = 0 
                                            """
            return query_string

        @staticmethod
        def reset_work_status_update_cmb():
            """rest record which hold work_status_update status in DB"""

            query_string = f"""
                                    UPDATE Saman_Monthly_Calc_Config  SET 
                                    is_work_status_updated = 0
                                    """
            return query_string

        @classmethod
        def reset(cls):
            """handle DB part of reset"""
            query_string_list = [
                cls.reset_calc_data(),
                cls.reset_total_sums(),
                cls.reset_work_status_update_cmb()
            ]
            query_string = ";".join(query_string_list)

            DBQuery.script_query(query_string)

