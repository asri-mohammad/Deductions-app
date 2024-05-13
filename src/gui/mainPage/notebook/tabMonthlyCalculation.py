from src.gui.abstraction.section import Section
from src.gui.mainPage.monthlyCalculation.settingSec import SettingSec
from src.gui.mainPage.monthlyCalculation.workStatusUpdateSec import WorkStatusUpdateSec
from src.gui.mainPage.monthlyCalculation.responseSec import ResponseSec
from src.gui.mainPage.monthlyCalculation.requestSec import RequestSec
from src.gui.mainPage.monthlyCalculation.bankSec import BankSec
from src.functionality.constants.constants import global_pad_y, global_pad_x, global_pad_left, global_pad_right,\
                                                                                global_pad_top, global_pad_bottom


class TabMonthlyCalculation(Section):
    def __init__(self, parent):
        self.lfr_setting_sec = None
        self.lfr_work_status_update_sec = None
        self.lfr_response_sec = None
        self.lfr_request_sec = None
        self.lfr_bank_sec = None
        super().__init__(parent)

    def create_components(self):
        self.lfr_setting_sec = SettingSec(self, "Period setting")
        self.lfr_work_status_update_sec = WorkStatusUpdateSec(self, "Work status update")
        self.lfr_response_sec = ResponseSec(self, "Responses")
        self.lfr_request_sec = RequestSec(self, "Requests list")
        self.lfr_bank_sec = BankSec(self, "Bank list")

    def register_components(self):
        pass

    def locate_components(self):
        self.lfr_setting_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_work_status_update_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_response_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_request_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_bank_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))