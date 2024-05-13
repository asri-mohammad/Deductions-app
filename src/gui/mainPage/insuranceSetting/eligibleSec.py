import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker


class EligibleSec(LabelSection):

    def __init__(self, parent, label):
        self.btn_insurance_eligible = None
        self.btn_insurance_eligible_update = None
        super().__init__(parent, label)

    def create_components(self):
        self.btn_insurance_eligible = tk.Button(self, text="Eligibles list")
        self.btn_insurance_eligible_update = tk.Button(self, text="Update")

    def register_components(self):
        GUITracker.set("monthly_calc_request_btn_insurance_eligible", self.btn_insurance_eligible)
        GUITracker.set("monthly_calc_request_btn_insurance_eligible_update", self.btn_insurance_eligible_update)

    def locate_components(self):
        self.btn_insurance_eligible.pack(side="top", fill="x")
        self.btn_insurance_eligible_update.pack(side="top", fill="x")