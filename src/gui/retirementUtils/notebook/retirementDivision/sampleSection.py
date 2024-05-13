import tkinter as tk
from src.gui.abstraction.section import Section
from src.gui.guiTracking.guiTracker import GUITracker


class SampleSection(Section):

    def __init__(self, parent):
        self.btn_sample = None
        super().__init__(parent)

    def create_components(self):
        self.btn_sample = tk.Button(self, text="Sample File")

    def register_components(self):
        GUITracker.set("division_btn_sample", self.btn_sample)

    def locate_components(self):
        self.btn_sample.pack(side="left", expand=1, fill="x")