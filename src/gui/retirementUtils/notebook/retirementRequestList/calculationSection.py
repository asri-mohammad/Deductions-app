import tkinter as tk
from src.gui.abstraction.section import Section
from src.gui.guiTracking.guiTracker import GUITracker


class CalculationSection(Section):

    def __init__(self, parent):
        self.btnCalculate = None
        super().__init__(parent)

    def create_components(self):
        self.btnCalculate = tk.Button(self, text="CALCULATE")

    def register_components(self):
        GUITracker.set("retirement_request_btn_calculate", self.btnCalculate)

    def locate_components(self):
        self.btnCalculate.pack(side="left", expand=1, fill="x")