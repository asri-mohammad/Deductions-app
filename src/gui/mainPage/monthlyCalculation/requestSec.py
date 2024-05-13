import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil


class RequestSec(LabelSection):

    def __init__(self, parent, label):
        self.btn_comptroller_req_list = None
        self.btn_retires_req_list = None
        self.btn_insurance_req_list = None

        super().__init__(parent, label)

    def create_components(self):
        self.btn_comptroller_req_list = tk.Button(self, text="Comptroller request list")
        self.btn_retires_req_list = tk.Button(self, text="Retires request list")
        self.btn_insurance_req_list = tk.Button(self, text="Insurance request list")

    def register_components(self):
        GUITracker.set("monthly_calc_request_btn_comptroller_req", self.btn_comptroller_req_list)
        GUITracker.set("monthly_calc_request_btn_retires_req", self.btn_retires_req_list)
        GUITracker.set("monthly_calc_request_btn_insurance_req", self.btn_insurance_req_list)

    def locate_components(self):

        self.btn_comptroller_req_list.pack(side="top", fill="x")
        self.btn_retires_req_list.pack(side="top", fill="x")
        self.btn_insurance_req_list.pack(side="top", fill="x")


