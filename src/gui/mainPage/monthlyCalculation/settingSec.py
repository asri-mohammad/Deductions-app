import tkinter as tk
from tkinter import ttk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.labelSection import LabelSection
from src.functionality.constants.constants import Periods


class SettingSec(LabelSection):

    def __init__(self, parent, label):
        self.btn_reset_period = None
        self.lbl_what_month = None
        self.cmb_period = None
        super().__init__(parent, label)

    def create_components(self):
        self.btn_reset_period = tk.Button(self, text="reset period")
        self.lbl_what_month = tk.Label(self, text="What month are we in: ")
        self.cmb_period = ttk.Combobox(self, values=Periods.period_lst, state="readonly")
        self.cmb_period.set(Periods.period_lst[0])

    def register_components(self):
        GUITracker.set("monthly_calculation_setting_btn_reset", self.btn_reset_period)
        GUITracker.set("monthly_calculation_setting_cmb_period", self.cmb_period)

    def locate_components(self):
        self.btn_reset_period.pack(side="top", expand=0, fill="x")
        self.lbl_what_month.pack(side="left", expand=0, fill="x")
        self.cmb_period.pack(side="top", expand=0, fill="x")
