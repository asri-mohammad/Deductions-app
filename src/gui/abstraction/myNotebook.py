from tkinter import ttk


class MyNotebook(ttk.Notebook):

    def __init__(self, prent):
        super().__init__(prent)
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