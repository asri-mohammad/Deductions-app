from src.gui.abstraction.myNotebook import MyNotebook
from src.gui.retirementUtils.notebook.tabRetirementDivision import TabRetirementDivision
from src.gui.retirementUtils.notebook.tabRetirementRequestList import TabRetirementRequestList


class MultiTab(MyNotebook):
    def __init__(self, parent):
        self.tab_retirement_division = None
        self.tab_retirement_request_list = None
        super().__init__(parent)

    def create_components(self):
        self.tab_retirement_division = TabRetirementDivision(self)
        self.tab_retirement_request_list = TabRetirementRequestList(self)

    def register_components(self):
        pass

    def locate_components(self):
        self.add(self.tab_retirement_division, text="Response division")
        self.add(self.tab_retirement_request_list, text="Request list")