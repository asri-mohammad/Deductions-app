import tkinter as tk

from src.gui.abstraction.section import Section
from src.gui.mainPage.batchOperation.updateSec import UpdateSec
from src.gui.mainPage.batchOperation.fullReportSec import FullReportSec
from src.functionality.constants.constants import global_pad_y, global_pad_x, global_pad_left, global_pad_right,\
                                                                                global_pad_top, global_pad_bottom


class TabBatchOperation(Section):
    def __init__(self, parent):
        self.lfr_update_sec = None
        self.lfr_full_report_sec = None

        super().__init__(parent)

    def create_components(self):
        self.lfr_update_sec = UpdateSec(self, "Update")
        self.lfr_full_report_sec = FullReportSec(self, "Full report")

    def register_components(self):
        pass

    def locate_components(self):
        pass
        self.lfr_update_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_full_report_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
