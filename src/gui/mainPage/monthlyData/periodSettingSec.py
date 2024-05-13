import tkinter as tk
from tkinter import ttk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.labelSection import LabelSection
from src.functionality.constants.constants import Periods
from src.functionality.util.guiUtil import GUIUtil


class PeriodSettingSec(LabelSection):

    def __init__(self, parent, label):
        self.lbl_month = None
        self.cmb_period = None
        self.btn_reset = None
        super().__init__(parent, label)

    def create_components(self):
        self.lbl_month = tk.Label(self, text="Month: ")
        self.cmb_period = ttk.Combobox(self, values=Periods.period_lst, state="readonly")
        self.cmb_period.set(Periods.period_lst[0])
        self.btn_reset = tk.Button(self, text="reset")

    def register_components(self):
        GUITracker.set("monthly_data_period_setting_cmb_period", self.cmb_period)
        GUITracker.set("monthly_data_period_setting_btn_reset", self.btn_reset)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 1, 3, [1], [1, 7, 2])

        self.lbl_month.grid(row=0, column=0, sticky="ew")
        self.cmb_period.grid(row=0, column=1, sticky="nesw")
        self.btn_reset.grid(row=0, column=2, sticky="nesw")
