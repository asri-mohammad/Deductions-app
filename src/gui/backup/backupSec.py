import tkinter as tk

from src.gui.abstraction.section import Section
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil



class BackupSec(Section):

    def __init__(self, prent):
        self.lbl_backup_dir = None
        self.ent_backup_dir = None
        self.btn_select_dir = None
        self.btn_export = None
        self.btn_import = None

        super().__init__(prent)

    def create_components(self):
        """a place to crated components belong to the frame """
        self.lbl_backup_dir = tk.Label(self, text="Backup folder :")
        self.ent_backup_dir = tk.Entry(self)
        self.btn_select_dir = tk.Button(self, text="Select folder")

        self.btn_export = tk.Button(self, text="<- Export ->")
        self.btn_import = tk.Button(self, text="-> Import <-")

    def register_components(self):
        """a place to add components to the global dictionary tracking GUI components"""
        GUITracker.set("backup_btn_select_dir", self.btn_select_dir)
        GUITracker.set("backup_ent_backup_dir", self.ent_backup_dir)

        GUITracker.set("backup_btn_export", self.btn_export)
        GUITracker.set("backup_btn_import", self.btn_import)

    def locate_components(self):
        """a place to locate components belong to the frame"""
        GUIUtil.divide_container_equally_custom_weight(self, 3, 3, [1, 1, 1], [1, 8, 1])

        self.lbl_backup_dir.grid(row=0, column=0, columnspan=1, sticky="nesw")
        self.ent_backup_dir.grid(row=0, column=1, columnspan=1, sticky="nesw")
        self.btn_select_dir.grid(row=0, column=2, columnspan=1, sticky="nesw")
        self.btn_export.grid(row=1, column=0, columnspan=3, sticky="nesw")
        self.btn_import.grid(row=2, column=0, columnspan=3, sticky="nesw")