import tkinter as tk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.section import Section
from src.functionality.util.guiUtil import GUIUtil


class BankSec(Section):

    def __init__(self, parent):
        self.btn_bank_list = None
        self.btn_bank_list_sample = None
        self.lbl_bank_list_sum = None

        self.btn_other = None
        self.btn_other_sample = None
        self.lbl_other_sum = None

        self.lbl_empty_1 = None
        self.lbl_empty_2 = None
        self.lbl_empty_3 = None

        self.lbl_total = None
        self.lbl_bank_sum = None

        super().__init__(parent)

    def create_components(self):

        self.btn_bank_list = tk.Button(self, text="Bank List")
        self.btn_bank_list_sample = tk.Button(self, text="sample")
        self.lbl_bank_list_sum = tk.Label(self, text="0")

        self.btn_other = tk.Button(self, text="Others")
        self.btn_other_sample = tk.Button(self, text="sample")
        self.lbl_other_sum = tk.Label(self, text="0")

        self.lbl_empty_1 = tk.Label(self, text=" ")  # TODO: this may needs a better solution
        self.lbl_empty_2 = tk.Label(self, text=" ")
        self.lbl_empty_3 = tk.Label(self, text=" ")

        self.lbl_total = tk.Label(self, text="Total: ")
        self.lbl_bank_sum = tk.Label(self, text="0")

    def register_components(self):
        GUITracker.set("monthly_data_data_btn_bank_list", self.btn_bank_list)
        GUITracker.set("monthly_data_data_btn_bank_list_sample", self.btn_bank_list_sample)
        GUITracker.set("monthly_data_data_lbl_bank_list", self.lbl_bank_list_sum)

        GUITracker.set("monthly_data_data_btn_other", self.btn_other)
        GUITracker.set("monthly_data_data_btn_other_sample", self.btn_other_sample)
        GUITracker.set("monthly_data_data_lbl_other", self.lbl_other_sum)

        GUITracker.set("monthly_data_data_lbl_bank_sum", self.lbl_bank_sum)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 6, 3, [1, 1, 1, 1, 1, 1], [4, 1, 4])

        self.btn_bank_list.grid(row=0, column=0, columnspan=1, sticky="nesw")
        self.btn_bank_list_sample.grid(row=0, column=1, columnspan=1, sticky="nesw")
        self.lbl_bank_list_sum.grid(row=0, column=2, columnspan=1, sticky="nesw")

        self.btn_other.grid(row=1, column=0, columnspan=1, sticky="nesw")
        self.btn_other_sample.grid(row=1, column=1, columnspan=1, sticky="nesw")
        self.lbl_other_sum.grid(row=1, column=2, columnspan=1, sticky="nesw")

        self.lbl_empty_1.grid(row=2, column=0, columnspan=3, sticky="nesw")
        self.lbl_empty_2.grid(row=3, column=0, columnspan=3, sticky="nesw")
        self.lbl_empty_3.grid(row=4, column=0, columnspan=3, sticky="nesw")

        self.lbl_total.grid(row=5, column=0, columnspan=2, sticky="nesw")
        self.lbl_bank_sum.grid(row=5, column=2, columnspan=1, sticky="nesw")
