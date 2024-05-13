import tkinter as tk
from tkinter import ttk
from tkinter import IntVar

from src.functionality.util.guiUtil import GUIUtil
from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker


class WorkStatusUpdateSec(LabelSection):

    def __init__(self, parent, label):
        self.btn_update = None
        self.btn_update_sample = None
        self.btn_unknown_list = None
        self.btn_unknown_list_sample = None
        self.is_work_status_updated_var = None
        self.chb_is_work_status_updated = None
        super().__init__(parent, label)

    def create_components(self):
        self.btn_update = tk.Button(self, text="Update work status")
        self.btn_update_sample = tk.Button(self, text="sample")
        self.btn_unknown_list = tk.Button(self, text="Unknown list")
        self.btn_unknown_list_sample = tk.Button(self, text="sample")
        self.is_work_status_updated_var = IntVar()
        self.chb_is_work_status_updated = tk.Checkbutton(self, text="Work statuses have been updated.",
                                                    variable=self.is_work_status_updated_var, onvalue=1, offvalue=0)

    def register_components(self):
        GUITracker.set("monthly_calculation_btn_work_status_update_sample", self.btn_update_sample)
        GUITracker.set("monthly_calculation_btn_work_status_update", self.btn_update)
        GUITracker.set("monthly_calculation_btn_unknown_list_sample", self.btn_unknown_list_sample)
        GUITracker.set("monthly_calculation_btn_unknown_list", self.btn_unknown_list)
        GUITracker.set("monthly_calculation_chb_is_work_status_updated", self.chb_is_work_status_updated)
        GUITracker.set("monthly_calculation_chb_var_is_work_status_updated", self.is_work_status_updated_var)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 3, 2, [1, 1, 1], [3, 1])
        self.btn_update.grid(row=0, column=0, sticky="nesw")
        self.btn_update_sample.grid(row=0, column=1, sticky="nesw")
        self.btn_unknown_list.grid(row=1, column=0, sticky="nesw")
        self.btn_unknown_list_sample.grid(row=1, column=1, sticky="nesw")
        self.chb_is_work_status_updated.grid(row=2, column=0, sticky="w")

