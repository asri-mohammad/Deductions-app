from src.gui.abstraction.section import Section
from src.gui.mainPage.insuranceSetting.eligibleSec import EligibleSec
from src.gui.mainPage.insuranceSetting.reasonSec import ReasonSec


class TabInsuranceSetting(Section):
    def __init__(self, parent):
        self.lfr_eligible_sec = None
        self.lfr_reason_sec = None

        super().__init__(parent)

    def create_components(self):
        self.lfr_eligible_sec = EligibleSec(self, "Eligible setting")
        self.lfr_reason_sec = ReasonSec(self, "Reason setting")

    def register_components(self):
        pass

    def locate_components(self):
        self.lfr_eligible_sec.pack(sid="top", fill="x")
        self.lfr_reason_sec.pack(side="top", fill="x")
