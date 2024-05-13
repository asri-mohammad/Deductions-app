from src.gui.guiTracking.guiTracker import GUITracker


class MonthlyDataUtil:

    @staticmethod
    def get_period(output_type="str"):
        """returns the value of period selection combobox, type in {str, int}"""

        period = GUITracker.get("monthly_data_period_setting_cmb_period").get()

        if output_type == "str":
            return period
        elif output_type == "int":
            return int(period)