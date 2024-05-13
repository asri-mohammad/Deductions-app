import tkinter as tk
from tkinter import ttk
from tkinter import IntVar

from src.functionality.util.guiUtil import GUIUtil
from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker


class ResponseSec(LabelSection):

    def __init__(self, parent, label):
        self.lbl_sum = None

        self.btn_comptroller_req = None
        self.btn_comptroller_req_sample = None
        self.lbl_comptroller_req_sum = None

        self.btn_comptroller_res = None
        self.btn_comptroller_res_sample = None
        self.lbl_comptroller_res_sum = None

        self.btn_retires_res = None
        self.btn_retires_res_sample = None
        self.lbl_retires_res_sum = None

        self.btn_insurance_res = None
        self.btn_insurance_res_sample = None
        self.lbl_insurance_res_sum = None

        self.btn_overdue_res = None
        self.btn_overdue_res_sample = None
        self.lbl_overdue_res_sum = None

        super().__init__(parent, label)

    def create_components(self):
        self.lbl_sum = tk.Label(self, text="SUM")

        self.btn_comptroller_req = tk.Button(self, text="Comptroller request (last month)")
        self.btn_comptroller_req_sample = tk.Button(self, text="sample")
        self.lbl_comptroller_req_sum = tk.Label(self, text="0")

        self.btn_comptroller_res = tk.Button(self, text="Comptroller response")
        self.btn_comptroller_res_sample = tk.Button(self, text="sample")
        self.lbl_comptroller_res_sum = tk.Label(self, text="0")

        self.btn_retires_res = tk.Button(self, text="Retires response")
        self.btn_retires_res_sample = tk.Button(self, text="sample")
        self.lbl_retires_res_sum = tk.Label(self, text="0")

        self.btn_insurance_res = tk.Button(self, text="Insurance response")
        self.btn_insurance_res_sample = tk.Button(self, text="sample")
        self.lbl_insurance_res_sum = tk.Label(self, text="0")

        self.btn_overdue_res = tk.Button(self, text="Overdue response")
        self.btn_overdue_res_sample = tk.Button(self, text="sample")
        self.lbl_overdue_res_sum = tk.Label(self, text="0")

    def register_components(self):
        GUITracker.set("monthly_calc_response_btn_comptroller_req", self.btn_comptroller_req)
        GUITracker.set("monthly_calc_response_btn_comptroller_req_sample", self.btn_comptroller_req_sample)
        GUITracker.set("monthly_calc_response_lbl_comptroller_req_sum", self.lbl_comptroller_req_sum)

        GUITracker.set("monthly_calc_response_btn_comptroller_res", self.btn_comptroller_res)
        GUITracker.set("monthly_calc_response_btn_comptroller_res_sample", self.btn_comptroller_res_sample)
        GUITracker.set("monthly_calc_response_lbl_comptroller_res_sum", self.lbl_comptroller_res_sum)

        GUITracker.set("monthly_calc_response_btn_retires_res", self.btn_retires_res)
        GUITracker.set("monthly_calc_response_btn_retires_res_sample", self.btn_retires_res_sample)
        GUITracker.set("monthly_calc_response_lbl_retires_res_sum", self.lbl_retires_res_sum)

        GUITracker.set("monthly_calc_response_btn_insurance_res", self.btn_insurance_res)
        GUITracker.set("monthly_calc_response_btn_insurance_res_sample", self.btn_insurance_res_sample)
        GUITracker.set("monthly_calc_response_lbl_insurance_res_sum", self.lbl_insurance_res_sum)

        GUITracker.set("monthly_calc_response_btn_overdue_res", self.btn_overdue_res)
        GUITracker.set("monthly_calc_response_btn_overdue_res_sample", self.btn_overdue_res_sample)
        GUITracker.set("monthly_calc_response_lbl_overdue_res_sum", self.lbl_overdue_res_sum)



    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 6, 3, [1, 1, 1, 1, 1, 1], [4, 1, 1])

        self.lbl_sum.grid(row=0, column=2, columnspan=1, sticky="nesw")

        self.btn_comptroller_req.grid(row=1, column=0, columnspan=1, sticky="nesw")
        self.btn_comptroller_req_sample.grid(row=1, column=1, columnspan=1, sticky="nesw")
        self.lbl_comptroller_req_sum.grid(row=1, column=2, columnspan=1, sticky="nesw")

        self.btn_comptroller_res.grid(row=2, column=0, columnspan=1, sticky="nesw")
        self.btn_comptroller_res_sample.grid(row=2, column=1, columnspan=1, sticky="nesw")
        self.lbl_comptroller_res_sum.grid(row=2, column=2, columnspan=1, sticky="nesw")

        self.btn_retires_res.grid(row=3, column=0, columnspan=1, sticky="nesw")
        self.btn_retires_res_sample.grid(row=3, column=1, columnspan=1, sticky="nesw")
        self.lbl_retires_res_sum.grid(row=3, column=2, columnspan=1, sticky="nesw")

        self.btn_insurance_res.grid(row=4, column=0, columnspan=1, sticky="nesw")
        self.btn_insurance_res_sample.grid(row=4, column=1, columnspan=1, sticky="nesw")
        self.lbl_insurance_res_sum.grid(row=4, column=2, columnspan=1, sticky="nesw")

        self.btn_overdue_res.grid(row=5, column=0, columnspan=1, sticky="nesw")
        self.btn_overdue_res_sample.grid(row=5, column=1, columnspan=1, sticky="nesw")
        self.lbl_overdue_res_sum.grid(row=5, column=2, columnspan=1, sticky="nesw")




