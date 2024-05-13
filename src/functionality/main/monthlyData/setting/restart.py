from src.functionality.main.monthlyData.setting.dataDisplay import DataDisplay
from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class Restart:

    @staticmethod
    @run_func_disp_err_ret_brk
    def reset():
        """resets gui and database"""

        GUIReset.reset_gui()
        cmb_period = GUITracker.get("monthly_data_period_setting_cmb_period")
        DBReset.reset_db(cmb_period)


class GUIReset:

    @staticmethod
    def reset_gui():
        """set the labels and note to the default value"""

        DataDisplay.set_all_to_default()


class DBReset:

    @staticmethod
    def get_period(cmb_widget):
        """given a combobox return combobox value as an integer"""

        period = cmb_widget.get()
        period = int(period)
        return period

    @staticmethod
    def reset_data(period):
        """delete all the data stored for the given month from table"""

        table_name = "Saman_Monthly_Data_Data"
        query_string = f"""
                            DELETE FROM {table_name} WHERE period = {period};
                        """
        DBQuery.dml_query(query_string)

    @staticmethod
    def reset_summary(period):
        """delete data summary row for the given period from table"""

        table_name = "Saman_Monthly_Data_Data_Summary"
        query_string = f"""
                            DELETE FROM {table_name} WHERE period = {period};
                        """
        DBQuery.dml_query(query_string)

    @classmethod
    def reset_db(cls, cmb_widget):
        """reads the period from the given widget and clean the database for that period"""

        period = cls.get_period(cmb_widget)
        cls.reset_summary(period)
        cls.reset_data(period)

