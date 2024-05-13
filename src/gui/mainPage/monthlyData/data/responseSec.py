import tkinter as tk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.section import Section
from src.functionality.util.guiUtil import GUIUtil


class ResponseSec(Section):

    def __init__(self, parent):
        self.btn_comptroller_res = None
        self.btn_comptroller_res_sample = None
        self.lbl_comptroller_res_sum = None

        self.btn_retires_res = None
        self.btn_retires_res_sample = None
        self.lbl_retires_res_sum = None

        self.btn_insurance_res = None
        self.btn_insurance_res_sample = None
        self.lbl_insurance_res_sum = None

        self.lbl_empty_1 = None
        self.lbl_empty_2 = None

        self.lbl_total = None
        self.lbl_res_sum = None

        super().__init__(parent)

    def create_components(self):

        self.btn_comptroller_res = tk.Button(self, text="Comptroller response")
        self.btn_comptroller_res_sample = tk.Button(self, text="sample")
        self.lbl_comptroller_res_sum = tk.Label(self, text="0")

        self.btn_retires_res = tk.Button(self, text="Retires response")
        self.btn_retires_res_sample = tk.Button(self, text="sample")
        self.lbl_retires_res_sum = tk.Label(self, text="0")

        self.btn_insurance_res = tk.Button(self, text="Insurance response")
        self.btn_insurance_res_sample = tk.Button(self, text="sample")
        self.lbl_insurance_res_sum = tk.Label(self, text="0")

        self.lbl_empty_1 = tk.Label(self, text=" ")  # TODO: this may needs a better solution
        self.lbl_empty_2 = tk.Label(self, text=" ")

        self.lbl_total = tk.Label(self, text="Total: ")
        self.lbl_res_sum = tk.Label(self, text="0")

    def register_components(self):
        GUITracker.set("monthly_data_data_btn_comptroller_res", self.btn_comptroller_res)
        GUITracker.set("monthly_data_data_btn_comptroller_res_sample", self.btn_comptroller_res_sample)
        GUITracker.set("monthly_data_data_lbl_comptroller_res", self.lbl_comptroller_res_sum)

        GUITracker.set("monthly_data_data_btn_retires_res", self.btn_retires_res)
        GUITracker.set("monthly_data_data_btn_retires_res_sample", self.btn_retires_res_sample)
        GUITracker.set("monthly_data_data_lbl_retires_res", self.lbl_retires_res_sum)

        GUITracker.set("monthly_data_data_btn_insurance_res", self.btn_insurance_res)
        GUITracker.set("monthly_data_data_btn_insurance_res_sample", self.btn_insurance_res_sample)
        GUITracker.set("monthly_data_data_lbl_insurance_res", self.lbl_insurance_res_sum)

        GUITracker.set("monthly_data_data_lbl_res_sum", self.lbl_res_sum)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 6, 3, [1, 1, 1, 1, 1, 1], [4, 1, 4])

        self.btn_comptroller_res.grid(row=0, column=0, columnspan=1, sticky="nesw")
        self.btn_comptroller_res_sample.grid(row=0, column=1, columnspan=1, sticky="nesw")
        self.lbl_comptroller_res_sum.grid(row=0, column=2, columnspan=1, sticky="nesw")

        self.btn_retires_res.grid(row=1, column=0, columnspan=1, sticky="nesw")
        self.btn_retires_res_sample.grid(row=1, column=1, columnspan=1, sticky="nesw")
        self.lbl_retires_res_sum.grid(row=1, column=2, columnspan=1, sticky="nesw")

        self.btn_insurance_res.grid(row=2, column=0, columnspan=1, sticky="nesw")
        self.btn_insurance_res_sample.grid(row=2, column=1, columnspan=1, sticky="nesw")
        self.lbl_insurance_res_sum.grid(row=2, column=2, columnspan=1, sticky="nesw")

        self.lbl_empty_1.grid(row=3, column=0, columnspan=3, sticky="nesw")
        self.lbl_empty_2.grid(row=4, column=0, columnspan=3, sticky="nesw")

        self.lbl_total.grid(row=5, column=0, columnspan=2, sticky="nesw")
        self.lbl_res_sum.grid(row=5, column=2, columnspan=1, sticky="nesw")
