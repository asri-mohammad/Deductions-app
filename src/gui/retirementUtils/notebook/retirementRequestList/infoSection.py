import tkinter as tk

from src.gui.abstraction.section import Section
from src.gui.guiTracking.guiTracker import GUITracker



class InfoSection(Section):

    def __init__(self, parent):
        self.txt_info = None
        super().__init__(parent)

    def create_components(self):
        self.txt_info = tk.Text(self, font=("Helvetica", 10))

    def register_components(self):
        GUITracker.set("retirement_request_txt_info", self.txt_info)

    def locate_components(self):
        self.txt_info.pack(side="left", expand=1, fill="both")