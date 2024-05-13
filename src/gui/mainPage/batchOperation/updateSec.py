import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.functionality.util.guiUtil import GUIUtil
from src.gui.guiTracking.guiTracker import GUITracker


class UpdateSec(LabelSection):

    def __init__(self, parent, label):
        self.btn_residue = None
        self.btn_residue_sample = None
        self.btn_general_status = None
        self.btn_general_status_sample = None

        super().__init__(parent, label)

    def create_components(self):
        self.btn_residue = tk.Button(self, text="Residue update")
        self.btn_residue_sample = tk.Button(self, text="sample")
        self.btn_general_status = tk.Button(self, text="General status update")
        self.btn_general_status_sample = tk.Button(self, text="sample")

    def register_components(self):

        GUITracker.set("batch_operation_update_btn_residue", self.btn_residue)
        GUITracker.set("batch_operation_update_btn_residue_sample", self.btn_residue_sample)
        GUITracker.set("batch_operation_update_btn_general_status", self.btn_general_status)
        GUITracker.set("batch_operation_update_btn_general_status_sample", self.btn_general_status_sample)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 2, 2, [1, 1], [7, 1])
        self.btn_residue.grid(row=0, column=0, columnspan=1, sticky="nesw")
        self.btn_residue_sample.grid(row=0, column=1, columnspan=1, sticky="nesw")
        self.btn_general_status.grid(row=1, column=0, columnspan=1, sticky="nesw")
        self.btn_general_status_sample.grid(row=1, column=1, columnspan=1, sticky="nesw")

