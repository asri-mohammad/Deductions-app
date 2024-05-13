from src.gui.retirementUtils.notebook.retirementRequestList.calculationSection import CalculationSection
from src.gui.retirementUtils.notebook.retirementRequestList.infoSection import InfoSection
from src.gui.retirementUtils.notebook.retirementRequestList.openSection import OpenSection
from src.gui.retirementUtils.notebook.retirementRequestList.sampleSection import SampleSection
from src.gui.retirementUtils.notebook.retirementRequestList.saveSection import SaveSection
from src.gui.abstraction.section import Section


class TabRetirementRequestList(Section):

    def __init__(self, parent):
        self.frm_sample_section = None
        self.frm_info_section = None
        self.frm_save_section = None
        self.frm_calculation_section = None
        self.frm_open_section = None
        super().__init__(parent)

    def create_components(self):
        self.frm_sample_section = SampleSection(self)
        self.frm_open_section = OpenSection(self)
        self.frm_calculation_section = CalculationSection(self)
        self.frm_save_section = SaveSection(self)
        self.frm_info_section = InfoSection(self)

    def register_components(self):
        pass

    def locate_components(self):
        self.frm_sample_section.pack(side="top", expand=0, fill="x")
        self.frm_open_section.pack(side="top", expand=0, fill="x")
        self.frm_calculation_section.pack(side="top", expand=0, fill="x")
        self.frm_save_section.pack(side="top", expand=0, fill="x")
        self.frm_info_section.pack(side="top", expand=1, fill="both")
