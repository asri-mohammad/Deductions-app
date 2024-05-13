import tkinter as tk
from tkinter import ttk


class LabelSection(ttk.Labelframe):

    def __init__(self, prent, label):
        super().__init__(prent, text=label)
        self.create_components()
        self.register_components()
        self.locate_components()

    def create_components(self):
        """a place to crated components belong to the frame """
        pass

    def register_components(self):
        """a place to add components to the global dictionary tracking GUI components"""
        pass

    def locate_components(self):
        """a place to locate components belong to the frame"""
        pass