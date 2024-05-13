import tkinter as tk
from src.gui.abstraction.section import Section
from src.gui.guiTracking.guiTracker import GUITracker


class OpenSection(Section):

    def __init__(self, parent):
        self.btn_open_file = None
        self.ent_file_path = None
        self.lbl_path = None
        super().__init__(parent)

    def create_components(self):
        self.lbl_path = tk.Label(self, text="File Path : ")
        self.ent_file_path = tk.Entry(self)
        self.btn_open_file = tk.Button(self, text="OPEN")

    def register_components(self):
        GUITracker.set("retirement_request_ent_filePath", self.ent_file_path)
        GUITracker.set("retirement_request_btn_openFile", self.btn_open_file)

    def locate_components(self):
        self.lbl_path.pack(side="left")
        self.ent_file_path.pack(side="left", expand=1, fill="x")
        self.btn_open_file.pack(side="left")