import tkinter as tk
from tkinter import IntVar

from src.gui.abstraction.labelSection import LabelSection
from src.gui.abstraction.section import Section
from src.functionality.util.guiUtil import GUIUtil
from src.gui.guiTracking.guiTracker import GUITracker


class FullReportSec(LabelSection):

    def __init__(self, parent, label):
        self.lbl_search_bar_title = None
        self.ent_search_bar = None
        self.frm_options = None
        self.btn_report_full_report = None

        super().__init__(parent, label)

    def create_components(self):
        self.lbl_search_bar_title = tk.Label(self, text="Search by employee ID :")
        self.ent_search_bar = tk.Entry(self)
        self.frm_options = CHBsFrame(self)
        self.btn_report_full_report = tk.Button(self, text="Full report")

    def register_components(self):
        GUITracker.set("batch_operation_full_report_ent_search_bar", self.ent_search_bar)
        GUITracker.set("batch_operation_full_report_btn_full_report", self.btn_report_full_report)

    def locate_components(self):
        self.lbl_search_bar_title.pack(side="top", expand=0, anchor="nw")
        self.ent_search_bar.pack(side="top", expand=0, fill="x")
        self.frm_options.pack(side="top", expand=0)
        self.btn_report_full_report.pack(side="top", expand=0, fill="x")


class CHBsFrame(Section):

    def __init__(self, parent):
        self.chb_employee_id = None
        self.chb_national_id = None
        self.chb_first_name = None
        self.chb_last_name = None
        self.chb_residue = None

        self.chb_general_status = None
        self.chb_work_status = None
        self.chb_loan_amount = None
        self.chb_installment_amount = None
        self.chb_file_number = None

        self.chb_employee_id_var = None
        self.chb_national_id_var = None
        self.chb_first_name_var = None
        self.chb_last_name_var = None
        self.chb_residue_var = None

        self.chb_general_status_var = None
        self.chb_work_status_var = None
        self.chb_loan_amount_var = None
        self.chb_installment_amount_var = None
        self.chb_file_number_var = None

        super().__init__(parent)

    def create_components(self):
        self.chb_employee_id_var = IntVar()
        self.chb_national_id_var = IntVar()
        self.chb_first_name_var = IntVar()
        self.chb_last_name_var = IntVar()
        self.chb_residue_var = IntVar()

        self.chb_general_status_var = IntVar()
        self.chb_work_status_var = IntVar()
        self.chb_loan_amount_var = IntVar()
        self.chb_installment_amount_var = IntVar()
        self.chb_file_number_var = IntVar()

        self.chb_employee_id = tk.Checkbutton(self, text="Employee ID", variable=self.chb_employee_id_var, onvalue=1,
                                              offvalue=0)
        self.chb_national_id = tk.Checkbutton(self, text="National ID", variable=self.chb_national_id_var, onvalue=1,
                                              offvalue=0)
        self.chb_first_name = tk.Checkbutton(self, text="First name", variable=self.chb_first_name_var, onvalue=1,
                                             offvalue=0)
        self.chb_last_name = tk.Checkbutton(self, text="Last Name", variable=self.chb_last_name_var, onvalue=1,
                                            offvalue=0)
        self.chb_residue = tk.Checkbutton(self, text="Residue", variable=self.chb_residue_var, onvalue=1, offvalue=0)

        self.chb_general_status = tk.Checkbutton(self, text="General status", variable=self.chb_general_status_var,
                                                 onvalue=1, offvalue=0)
        self.chb_work_status = tk.Checkbutton(self, text="work status", variable=self.chb_work_status_var, onvalue=1, offvalue=0)
        self.chb_loan_amount = tk.Checkbutton(self, text="Loan amount", variable=self.chb_loan_amount_var, onvalue=1,
                                              offvalue=0)
        self.chb_installment_amount = tk.Checkbutton(self, text="Installment amount",
                                                     variable=self.chb_installment_amount_var, onvalue=1, offvalue=0)
        self.chb_file_number = tk.Checkbutton(self, text="File number", variable=self.chb_file_number_var, onvalue=1,
                                              offvalue=0)

    def register_components(self):
        GUITracker.set("batch_operation_full_report_chb_var_employee_id", self.chb_employee_id_var)
        GUITracker.set("batch_operation_full_report_chb_var_national_id", self.chb_national_id_var)
        GUITracker.set("batch_operation_full_report_chb_var_first_name", self.chb_first_name_var)
        GUITracker.set("batch_operation_full_report_chb_var_last_name", self.chb_last_name_var)
        GUITracker.set("batch_operation_full_report_chb_var_residue", self.chb_residue_var)

        GUITracker.set("batch_operation_full_report_chb_var_general_status", self.chb_general_status_var)
        GUITracker.set("batch_operation_full_report_chb_var_work_status", self.chb_work_status_var)
        GUITracker.set("batch_operation_full_report_chb_var_loan_amount", self.chb_loan_amount_var)
        GUITracker.set("batch_operation_full_report_chb_var_installment_amount", self.chb_installment_amount_var)
        GUITracker.set("batch_operation_full_report_chb_var_file_number", self.chb_file_number_var)

    def locate_components(self):
        GUIUtil.divide_container_equally_custom_weight(self, 2, 5, [1] * 3, [1] * 5)
        pad_x_l = 50
        self.chb_employee_id.grid(row=0, column=0, columnspan=1, sticky="w")
        self.chb_national_id.grid(row=0, column=1, columnspan=1, sticky="w", padx=(pad_x_l, 0))
        self.chb_first_name.grid(row=0, column=2, columnspan=1, sticky="w", padx=(pad_x_l, 0))
        self.chb_last_name.grid(row=0, column=3, columnspan=1, sticky="w", padx=(pad_x_l, 0))
        self.chb_residue.grid(row=0, column=4, columnspan=1, sticky="w", padx=(pad_x_l, 0))

        self.chb_general_status.grid(row=1, column=0, columnspan=1, sticky="w")
        self.chb_work_status.grid(row=1, column=1, columnspan=1, sticky="w", padx=(pad_x_l, 0))
        self.chb_loan_amount.grid(row=1, column=2, columnspan=1, sticky="w", padx=(pad_x_l, 0))
        self.chb_installment_amount.grid(row=1, column=3, columnspan=1, sticky="w", padx=(pad_x_l, 0))
        self.chb_file_number.grid(row=1, column=4, columnspan=1, sticky="w", padx=(pad_x_l, 0))


