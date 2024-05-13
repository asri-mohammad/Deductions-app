import tkinter as tk

from src.gui.abstraction.section import Section
from src.gui.mainPage.info.searchSec import SearchSec
from src.gui.mainPage.info.personalInfoSec import PersonalInfoSec
from src.gui.mainPage.info.generalStatusSec import GeneralStatusSec
from src.functionality.constants.constants import global_pad_y, global_pad_x, global_pad_left, global_pad_right,\
                                                                                global_pad_top, global_pad_bottom


class TabInfo(Section):
    def __init__(self, parent):
        self.lfr_search_sec = None
        self.lfr_personal_info_sec = None
        self.lfr_general_status_sec = None
        super().__init__(parent)

    def create_components(self):
        self.lfr_search_sec = SearchSec(self, "Search user")
        self.lfr_personal_info_sec = PersonalInfoSec(self, "User information")
        self.lfr_general_status_sec = GeneralStatusSec(self, "General status")

    def register_components(self):
        pass

    def locate_components(self):
        self.lfr_search_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_personal_info_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_general_status_sec.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))