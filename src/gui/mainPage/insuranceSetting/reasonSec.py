import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker


class ReasonSec(LabelSection):

    def __init__(self, parent, label):
        self.btn_insurance_reasons = None
        self.btn_insurance_reasons_update = None

        super().__init__(parent, label)

    def create_components(self):
        self.btn_insurance_reasons = tk.Button(self, text="Reasons")
        self.btn_insurance_reasons_update = tk.Button(self, text="Update")

    def register_components(self):
        GUITracker.set("monthly_calc_request_btn_insurance_reasons", self.btn_insurance_reasons)
        GUITracker.set("monthly_calc_request_btn_insurance_reasons_update", self.btn_insurance_reasons_update)

    def locate_components(self):
        self.btn_insurance_reasons.pack(side="top", fill="x")
        self.btn_insurance_reasons_update.pack(side="top", fill="x")