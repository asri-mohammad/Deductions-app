import tkinter as tk
from src.gui.abstraction.section import Section
from src.gui.guiTracking.guiTracker import GUITracker


class SaveSection(Section):

    def __init__(self, parent):
        self.btn_save = None
        super().__init__(parent)

    def create_components(self):
        self.btn_save = tk.Button(self, text="SAVE")

    def register_components(self):
        GUITracker.set("division_btn_save", self.btn_save)

    def locate_components(self):
        self.btn_save.pack(side="left", expand=1, fill="x")