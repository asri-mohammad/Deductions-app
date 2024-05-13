import tkinter as tk

from src.gui.guiTracking.guiTracker import GUITracker
from src.gui.retirementUtils.notebook.multiTab import MultiTab as MultiTab_retirement_utils
from src.gui.mainPage.notebook.multiTab import MultiTab as MultiTab_main_page
from src.gui.backup.backup import Backup
from src.gui.menu.menu import Menu


class MainWindow(tk.Tk):

    def __init__(self, title, dimension):
        self.multi_tab_main_page = None
        self.multi_tab_retirement_utils = None
        self.frm_backup = None
        self.men_menu = None
        super().__init__()
        self.title(title)
        self.geometry(dimension)
        # creation and locating
        self.create_components()
        self.register_components()
        self.locate_components()

    def create_components(self):
        self.men_menu = Menu(self)
        # one that is created the last is shown above the others
        self.frm_backup = Backup(self)
        self.multi_tab_retirement_utils = MultiTab_retirement_utils(self)
        self.multi_tab_main_page = MultiTab_main_page(self)

    def register_components(self):
        GUITracker.set("root", self)
        GUITracker.set("multi_tab_retirement_utils", self.multi_tab_retirement_utils)
        GUITracker.set("multi_tab_main_page", self.multi_tab_main_page)
        GUITracker.set("frm_backup", self.frm_backup)

    def locate_components(self):
        self.men_menu.initialize()

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.multi_tab_retirement_utils.grid(row=0, column=0, sticky="news")
        self.multi_tab_main_page.grid(row=0, column=0, sticky="news")
        self.frm_backup.grid(row=0, column=0, sticky="nesw")




