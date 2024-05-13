from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.main.monthlyData.setting.periodSelection import PeriodSelection
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class MonthlyData:

    @classmethod
    def initialize(cls):
        """all the actions that should be done when the app start up"""

        period = cls.Period.get()
        cls.DataDisplay.display(period)
        cls.PeriodSetting.set(period)

    class DataDisplay:

        @staticmethod
        def display(period):
            """displaying data for the selected month in combobox"""

            data_summary = PeriodSelection.DataRetrieval.retrieve(period)
            PeriodSelection.DisplayData.display(data_summary)

    class PeriodSetting:
        @staticmethod
        def set(period):
            """set the value for the period selection combobox in monthly calculation section"""

            period_combobox = GUITracker.get("monthly_data_period_setting_cmb_period")
            period_combobox.set(period)

    class Period:

        @staticmethod
        def get():
            """gets the last period that was stored in DB"""

            period = DBQuery.dql_query("SELECT period FROM Saman_Monthly_Data_Config WHERE row_id = 1;")[0][0]
            return period



