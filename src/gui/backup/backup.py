import tkinter as tk

from src.gui.abstraction.section import Section
from src.gui.backup.backupSec import BackupSec


class Backup(Section):

    def __init__(self, prent):
        self.frm_backup_sec = None
        super().__init__(prent)

    def create_components(self):
        """a place to crated components belong to the frame """
        self.frm_backup_sec = BackupSec(self)

    def register_components(self):
        """a place to add components to the global dictionary tracking GUI components"""
        pass

    def locate_components(self):
        """a place to locate components belong to the frame"""
        self.frm_backup_sec.pack(side="top", fill="x")