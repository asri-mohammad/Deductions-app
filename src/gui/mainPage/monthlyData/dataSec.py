import tkinter as tk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.labelSection import LabelSection
from src.functionality.util.guiUtil import GUIUtil
from src.gui.mainPage.monthlyData.data.responseSec import ResponseSec
from src.gui.mainPage.monthlyData.data.requestSec import RequestSec
from src.gui.mainPage.monthlyData.data.bankSec import BankSec


class DataSec(LabelSection):

    def __init__(self, parent, label):
        self.frm_response_sec = None
        self.frm_request_sec = None
        self.frm_bank_sec = None
        self.btn_monthly_report = None

        super().__init__(parent, label)

    def create_components(self):
        self.frm_response_sec = ResponseSec(self)
        self.frm_request_sec = RequestSec(self)
        self.frm_bank_sec = BankSec(self)
        self.btn_monthly_report = tk.Button(self, text="Monthly report")

    def register_components(self):
        GUITracker.set("monthly_data_data_btn_monthly_report", self.btn_monthly_report)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 2, 3, [1, 1], [1, 1, 1])

        self.frm_response_sec.grid(row=0, column=0, sticky="nesw")
        self.frm_bank_sec.grid(row=0, column=1, sticky="nesw")
        self.frm_request_sec.grid(row=0, column=2, sticky="nesw")
        self.btn_monthly_report.grid(row=1, column=0, columnspan=3, sticky="nesw")
