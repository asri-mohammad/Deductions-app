import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker


class SearchSec(LabelSection):

    def __init__(self, parent, label):
        self.ent_search = None
        self.btn_search = None
        self.lbl_message = None
        super().__init__(parent, label)

    def create_components(self):
        self.ent_search = tk.Entry(self)
        self.btn_search = tk.Button(self, text="Search")
        self.lbl_message = tk.Label(self)

    def register_components(self):
        GUITracker.set("info_search_ent_search", self.ent_search)
        GUITracker.set("info_search_btn_search", self.btn_search)
        GUITracker.set("info_search_lbl_message", self.lbl_message)

    def locate_components(self):
        self.columnconfigure(0, weight=4, uniform="a")
        self.columnconfigure(1, weight=1, uniform="a")

        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")

        self.ent_search.grid(row=0, column=0, sticky="nesw")
        self.btn_search.grid(row=0, column=1, sticky="nesw")
        self.lbl_message.grid(row=1, column=0, columnspan=2, sticky="nesw")