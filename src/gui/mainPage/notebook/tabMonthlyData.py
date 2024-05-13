from src.gui.abstraction.section import Section

from src.gui.mainPage.monthlyData.periodSettingSec import PeriodSettingSec
from src.gui.mainPage.monthlyData.dataSec import DataSec
from src.gui.mainPage.monthlyData.noteSec import NoteSec
from src.functionality.constants.constants import global_pad_y, global_pad_x, global_pad_left, global_pad_right,\
                                                                                global_pad_top, global_pad_bottom


class TabMonthlyData(Section):
    def __init__(self, parent):
        self.lfr_period_setting = None
        self.lfr_data = None
        self.frm_note = None

        super().__init__(parent)

    def create_components(self):
        self.lfr_period_setting = PeriodSettingSec(self, "Period setting")
        self.lfr_data = DataSec(self, "Data")
        self.frm_note = NoteSec(self)

    def register_components(self):
        pass

    def locate_components(self):
        self.lfr_period_setting.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.lfr_data.pack(side="top", expand=0, fill="x", padx=global_pad_x, pady=(global_pad_top, 0))
        self.frm_note.pack(side="top", expand=1, fill="both", padx=global_pad_x, pady=(global_pad_top, 0))