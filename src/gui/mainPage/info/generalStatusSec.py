import tkinter as tk

from src.functionality.util.guiUtil import GUIUtil
from src.gui.abstraction.labelSection import LabelSection
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.constants.constants import GeneralStatusEnum


class GeneralStatusSec(LabelSection):

    def __init__(self, parent, label):
        self.radio_btn_var = tk.StringVar(value=str(GeneralStatusEnum.active.value))
        self.rbt_active = None
        self.rbt_settled = None
        self.rbt_passed_away = None
        self.rbt_temp_stop = None
        self.btn_register = None
        super().__init__(parent, label)

    def create_components(self):
        self.rbt_active = tk.Radiobutton(self, text="Active", variable=self.radio_btn_var, value=str(GeneralStatusEnum.active.value))
        self.rbt_settled = tk.Radiobutton(self, text="Settled", variable=self.radio_btn_var, value=str(GeneralStatusEnum.settled.value))
        self.rbt_passed_away = tk.Radiobutton(self, text="Passed away", variable=self.radio_btn_var, value=str(GeneralStatusEnum.passed_away.value))
        self.rbt_temp_stop = tk.Radiobutton(self, text="Temporary stop", variable=self.radio_btn_var, value=str(GeneralStatusEnum.temp_stop.value))
        self.btn_register = tk.Button(self, text="Register")

    def register_components(self):
        GUITracker.set("general_status_btn_register", self.btn_register)
        GUITracker.set("general_status_rbt_var", self.radio_btn_var)


    def locate_components(self):
        GUIUtil.divide_container_equally(self, 2, 4)
        self.rbt_active.grid(row=0, column=0)
        self.rbt_settled.grid(row=0, column=1)
        self.rbt_passed_away.grid(row=0, column=2)
        self.rbt_temp_stop.grid(row=0, column=3)
        self.btn_register.grid(row=1, column=0, columnspan=4, sticky="nesw")