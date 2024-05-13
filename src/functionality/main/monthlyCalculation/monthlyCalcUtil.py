from src.gui.guiTracking.guiTracker import GUITracker


class MonthlyCalcUtil:

    @staticmethod
    def get_period(output_type="str"):
        """returns the value of period selection combobox, type in {str, int}"""

        period = GUITracker.get("monthly_calculation_setting_cmb_period").get()

        if output_type == "str":
            return period
        elif output_type == "int":
            return int(period)

    @staticmethod
    def work_status_update_state():
        """return 1 if work status checkbox is checked, otherwise 0"""

        return GUITracker.get("monthly_calculation_chb_var_is_work_status_updated").get()
