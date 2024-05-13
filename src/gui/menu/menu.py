import tkinter as tk
from src.gui.guiTracking.guiTracker import GUITracker


class Menu:

    def __init__(self, parent):
        self.parent = parent

    def initialize(self):
        """where the whole menu is created and gets added to main window"""
        men_menubar = tk.Menu(self.parent)

        men_applications = tk.Menu(men_menubar, tearoff=0)
        men_menubar.add_cascade(label="Applications", menu=men_applications)
        # TODO : this class my needs a refactor and the following registration may relocate
        GUITracker.set("men_applications", men_applications)

        # applications
        men_applications.add_command(label="Main")
        men_applications.add_command(label="Retires utils")
        men_applications.add_command(label="Backup")

        self.parent.config(menu=men_menubar)

