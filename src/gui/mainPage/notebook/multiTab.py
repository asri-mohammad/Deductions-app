from src.gui.abstraction.myNotebook import MyNotebook
from src.gui.mainPage.notebook.tabInfo import TabInfo
from src.gui.mainPage.notebook.tabMonthlyCalculation import TabMonthlyCalculation
from src.gui.mainPage.notebook.tabMonthlyData import TabMonthlyData
from src.gui.mainPage.notebook.tabBatchOperation import TabBatchOperation
from src.gui.mainPage.notebook.tabInsuranceSetting import TabInsuranceSetting


class MultiTab(MyNotebook):
    def __init__(self, parent):
        self.tab_info = None
        self.tab_monthly_calculation = None
        self.tab_monthly_data = None
        self.tab_batch_operation = None
        self.tab_insurance_setting = None

        super().__init__(parent)

    def create_components(self):
        self.tab_info = TabInfo(self)
        self.tab_monthly_calculation = TabMonthlyCalculation(self)
        self.tab_monthly_data = TabMonthlyData(self)
        self.tab_batch_operation = TabBatchOperation(self)
        self.tab_insurance_setting = TabInsuranceSetting(self)

    def register_components(self):
        pass

    def locate_components(self):
        self.add(self.tab_info, text="Info")
        self.add(self.tab_monthly_calculation, text="Monthly calculation")
        self.add(self.tab_monthly_data, text="Monthly data")
        self.add(self.tab_batch_operation, text="Batch operation")
        self.add(self.tab_insurance_setting, text="Insurance setting")