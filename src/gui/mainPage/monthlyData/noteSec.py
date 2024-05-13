import tkinter as tk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.abstraction.section import Section


class NoteSec(Section):
    def __init__(self, parent):
        self.lbl_note = None
        self.frm_note = None
        self.btn_save = None

        super().__init__(parent)

    def create_components(self):
        self.lbl_note = tk.Label(self, text="Note : ")
        self.frm_note = NoteTextBox(self)
        self.btn_save = tk.Button(self, text="Save")

    def register_components(self):
        GUITracker.set("monthly_data_note_btn_save", self.btn_save)

    def locate_components(self):
        self.lbl_note.pack(side="top", anchor="w")
        self.frm_note.pack(side="top", expand=1, fill="both")
        self.btn_save.pack(side="top", expand=0, fill="x", pady=(5, 0))


class NoteTextBox(Section):

    def __init__(self, parent):

        self.scr_note = None
        self.txt_note = None

        super().__init__(parent)

    def create_components(self):
        self.scr_note = tk.Scrollbar(self)
        self.txt_note = tk.Text(self, height=1, yscrollcommand=self.scr_note.set, font=("Helvetica", 10))  # Todo: set a font obj
        self.scr_note.config(command=self.txt_note.yview)

    def register_components(self):
        GUITracker.set("monthly_data_note_txt_note", self.txt_note)
        pass

    def locate_components(self):
        self.txt_note.pack(side="left", expand=1, fill="both")
        self.scr_note.pack(side="left", fill="y")
