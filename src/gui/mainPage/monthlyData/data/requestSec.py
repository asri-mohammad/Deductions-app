import tkinter as tk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.section import Section
from src.functionality.util.guiUtil import GUIUtil


class RequestSec(Section):

    def __init__(self, parent):
        
        self.btn_overdue_res = None
        self.btn_overdue_res_sample = None
        self.lbl_overdue_res_sum = None
        
        self.btn_comptroller_req = None
        self.btn_comptroller_req_sample = None
        self.lbl_comptroller_req_sum = None

        self.btn_retires_req = None
        self.btn_retires_req_sample = None
        self.lbl_retires_req_sum = None

        self.btn_insurance_req = None
        self.btn_insurance_req_sample = None
        self.lbl_insurance_req_sum = None

        self.lbl_empty_1 = None

        self.lbl_total = None
        self.lbl_req_sum = None

        super().__init__(parent)

    def create_components(self):
        
        self.btn_overdue_res = tk.Button(self, text="Overdue")
        self.btn_overdue_res_sample = tk.Button(self, text="sample")
        self.lbl_overdue_res_sum = tk.Label(self, text="0", bg='gray')

        self.btn_comptroller_req = tk.Button(self, text="Comptroller request")
        self.btn_comptroller_req_sample = tk.Button(self, text="sample")
        self.lbl_comptroller_req_sum = tk.Label(self, text="0")

        self.btn_retires_req = tk.Button(self, text="Retires request")
        self.btn_retires_req_sample = tk.Button(self, text="sample")
        self.lbl_retires_req_sum = tk.Label(self, text="0")

        self.btn_insurance_req = tk.Button(self, text="Insurance request")
        self.btn_insurance_req_sample = tk.Button(self, text="sample")
        self.lbl_insurance_req_sum = tk.Label(self, text="0")

        self.lbl_empty_1 = tk.Label(self, text=" ")  # TODO: this may needs a better solution

        self.lbl_total = tk.Label(self, text="Total: ")
        self.lbl_req_sum = tk.Label(self, text="0")

    def register_components(self):
        GUITracker.set("monthly_data_data_btn_overdue_res", self.btn_overdue_res)
        GUITracker.set("monthly_data_data_btn_overdue_res_sample", self.btn_overdue_res_sample)
        GUITracker.set("monthly_data_data_lbl_overdue_res", self.lbl_overdue_res_sum)

        GUITracker.set("monthly_data_data_btn_comptroller_req", self.btn_comptroller_req)
        GUITracker.set("monthly_data_data_btn_comptroller_req_sample", self.btn_comptroller_req_sample)
        GUITracker.set("monthly_data_data_lbl_comptroller_req", self.lbl_comptroller_req_sum)

        GUITracker.set("monthly_data_data_btn_retires_req", self.btn_retires_req)
        GUITracker.set("monthly_data_data_btn_retires_req_sample", self.btn_retires_req_sample)
        GUITracker.set("monthly_data_data_lbl_retires_req", self.lbl_retires_req_sum)

        GUITracker.set("monthly_data_data_btn_insurance_req", self.btn_insurance_req)
        GUITracker.set("monthly_data_data_btn_insurance_req_sample", self.btn_insurance_req_sample)
        GUITracker.set("monthly_data_data_lbl_insurance_req", self.lbl_insurance_req_sum)

        GUITracker.set("monthly_data_data_lbl_req_sum", self.lbl_req_sum)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 6, 3, [1, 1, 1, 1, 1, 1], [4, 1, 4])
        
        self.btn_overdue_res.grid(row=0, column=0, columnspan=1, sticky="nesw")
        self.btn_overdue_res_sample.grid(row=0, column=1, columnspan=1, sticky="nesw")
        self.lbl_overdue_res_sum.grid(row=0, column=2, columnspan=1, sticky="nesw")

        self.btn_comptroller_req.grid(row=1, column=0, columnspan=1, sticky="nesw")
        self.btn_comptroller_req_sample.grid(row=1, column=1, columnspan=1, sticky="nesw")
        self.lbl_comptroller_req_sum.grid(row=1, column=2, columnspan=1, sticky="nesw")

        self.btn_retires_req.grid(row=2, column=0, columnspan=1, sticky="nesw")
        self.btn_retires_req_sample.grid(row=2, column=1, columnspan=1, sticky="nesw")
        self.lbl_retires_req_sum.grid(row=2, column=2, columnspan=1, sticky="nesw")

        self.btn_insurance_req.grid(row=3, column=0, columnspan=1, sticky="nesw")
        self.btn_insurance_req_sample.grid(row=3, column=1, columnspan=1, sticky="nesw")
        self.lbl_insurance_req_sum.grid(row=3, column=2, columnspan=1, sticky="nesw")

        self.lbl_empty_1.grid(row=4, column=0, columnspan=3, sticky="nesw")

        self.lbl_total.grid(row=5, column=0, columnspan=2, sticky="nesw")
        self.lbl_req_sum.grid(row=5, column=2, columnspan=1, sticky="nesw")
