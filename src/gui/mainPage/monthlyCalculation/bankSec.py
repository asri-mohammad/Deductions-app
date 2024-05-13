import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.functionality.util.guiUtil import GUIUtil
from src.gui.guiTracking.guiTracker import GUITracker


class BankSec(LabelSection):

    def __init__(self, parent, label):
        self.chb_employees = None
        self.chb_employees_var = None
        self.chb_retires = None
        self.chb_retires_var = None
        self.chb_insurance = None
        self.chb_insurance_var = None
        self.btn_bank_list = None
        self.ent_date = None
        self.btn_letter = None
        super().__init__(parent, label)

    def create_components(self):
        self.chb_employees_var = tk.IntVar()
        self.chb_employees = tk.Checkbutton(self, text="employees",
                                            variable=self.chb_employees_var, onvalue=1, offvalue=0)
        self.chb_retires_var = tk.IntVar()
        self.chb_retires = tk.Checkbutton(self, text="retires",
                                                  variable=self.chb_retires_var, onvalue=1, offvalue=0)
        self.chb_insurance_var = tk.IntVar()
        self.chb_insurance = tk.Checkbutton(self, text="insurance",
                                                  variable=self.chb_insurance_var, onvalue=1, offvalue=0)
        self.btn_bank_list = tk.Button(self, text="Generate the bank list")
        self.btn_letter = tk.Button(self, text="Bank letter")

    def register_components(self):

        GUITracker.set("monthly_calc_bank_list_chb_var_employees", self.chb_employees_var)
        GUITracker.set("monthly_calc_bank_list_chb_var_retires", self.chb_retires_var)
        GUITracker.set("monthly_calc_bank_list_chb_var_insurance", self.chb_insurance_var)
        GUITracker.set("monthly_calc_bank_list_btn_generate", self.btn_bank_list)
        GUITracker.set("monthly_calc_bank_list_btn_letter", self.btn_letter)

    def locate_components(self):
        GUIUtil.divide_container_equally(self, 3, 3)
        self.chb_employees.grid(row=0, column=0, columnspan=1, sticky="nesw")
        self.chb_retires.grid(row=0, column=1, columnspan=1, sticky="nesw")
        self.chb_insurance.grid(row=0, column=2, columnspan=1, sticky="nesw")
        self.btn_bank_list.grid(row=1, column=0, columnspan=3, sticky="nesw")
        self.btn_letter.grid(row=2, column=0, columnspan=3, sticky="nesw")
