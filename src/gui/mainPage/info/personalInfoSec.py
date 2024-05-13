import tkinter as tk

from src.gui.abstraction.labelSection import LabelSection
from src.functionality.util.guiUtil import GUIUtil
from src.gui.guiTracking.guiTracker import GUITracker


class PersonalInfoSec(LabelSection):

    def __init__(self, parent, label):
        # first row
        self.lbl_loan_recipient = None
        self.lbl_loan_recipient_result = None
        self.lbl_employee_id = None
        self.lbl_employee_id_result = None
        self.lbl_national_id = None
        self.lbl_national_id_result = None
        self.lbl_general_status = None
        self.lbl_general_status_result = None

        # second row
        self.lbl_bank = None
        self.lbl_bank_result = None
        self.lbl_branch = None
        self.lbl_branch_result = None
        self.lbl_loan_amount = None
        self.lbl_loan_amount_result = None
        self.lbl_installment_amount = None
        self.lbl_installment_amount_result = None

        # third row
        self.lbl_account_number = None
        self.lbl_account_number_result = None
        self.lbl_file_number = None
        self.lbl_file_number_result = None
        self.lbl_installment_count = None
        self.lbl_installment_count_result = None
        self.lbl_total_payment = None
        self.lbl_total_payment_result = None

        # fourth row
        self.lbl_starting_date = None
        self.lbl_starting_date_result = None
        self.lbl_ending_date = None
        self.lbl_ending_date_result = None
        self.lbl_loan_count = None
        self.lbl_loan_count_result = None
        self.lbl_work_status = None
        self.lbl_work_status_result = None

        # fifth row
        self.btn_report = None

        super().__init__(parent, label)

    def create_components(self):
        # first row
        self.lbl_loan_recipient = tk.Label(self, text="Loan recipient: ")
        self.lbl_loan_recipient_result = tk.Label(self, text=" ")
        self.lbl_employee_id = tk.Label(self, text="Employee ID: ")
        self.lbl_employee_id_result = tk.Label(self, text=" ")
        self.lbl_national_id = tk.Label(self, text="National ID: ")
        self.lbl_national_id_result = tk.Label(self, text=" ")
        self.lbl_general_status = tk.Label(self, text="General status: ")
        self.lbl_general_status_result = tk.Label(self, text=" ")

        # second row
        self.lbl_bank = tk.Label(self, text="Bank: ")
        self.lbl_bank_result = tk.Label(self, text=" ")
        self.lbl_branch = tk.Label(self, text="Branch: ")
        self.lbl_branch_result = tk.Label(self, text=" ")
        self.lbl_loan_amount = tk.Label(self, text="Loan amount: ")
        self.lbl_loan_amount_result = tk.Label(self, text=" ")
        self.lbl_installment_amount = tk.Label(self, text="Installment amount: ")
        self.lbl_installment_amount_result = tk.Label(self, text=" ")

        # third row
        self.lbl_account_number = tk.Label(self, text="Account Num: ")
        self.lbl_account_number_result = tk.Label(self, text=" ")
        self.lbl_file_number = tk.Label(self, text="File Num: ")
        self.lbl_file_number_result = tk.Label(self, text=" ")
        self.lbl_installment_count = tk.Label(self, text="Installment count: ")
        self.lbl_installment_count_result = tk.Label(self, text=" ")
        self.lbl_total_payment = tk.Label(self, text="Total payment: ")
        self.lbl_total_payment_result = tk.Label(self, text=" ")

        # fourth row
        self.lbl_starting_date = tk.Label(self, text="Starting Date: ")
        self.lbl_starting_date_result = tk.Label(self, text=" ")
        self.lbl_ending_date = tk.Label(self, text="Ending date: ")
        self.lbl_ending_date_result = tk.Label(self, text=" ")
        self.lbl_loan_count = tk.Label(self, text="Loan Count: ")
        self.lbl_loan_count_result = tk.Label(self, text=" ")
        self.lbl_work_status = tk.Label(self, text="work status: ")
        self.lbl_work_status_result = tk.Label(self, text=" ")

        # fifth row
        self.btn_report = tk.Button(self, text="Report")

    def register_components(self):
        GUITracker.set("personal_info_lbl_loan_recipient_result", self.lbl_loan_recipient_result)
        GUITracker.set("personal_info_lbl_employee_id_result", self.lbl_employee_id_result)
        GUITracker.set("personal_info_lbl_national_id_result", self.lbl_national_id_result)
        GUITracker.set("personal_info_lbl_general_status_result", self.lbl_general_status_result)

        GUITracker.set("personal_info_lbl_bank_result", self.lbl_bank_result)
        GUITracker.set("personal_info_lbl_branch_result", self.lbl_branch_result)
        GUITracker.set("personal_info_lbl_loan_amount_result", self.lbl_loan_amount_result)
        GUITracker.set("personal_info_lbl_installment_amount_result", self.lbl_installment_amount_result)

        GUITracker.set("personal_info_lbl_account_number_result", self.lbl_account_number_result)
        GUITracker.set("personal_info_lbl_file_number_result", self.lbl_file_number_result)
        GUITracker.set("personal_info_lbl_installment_count_result", self.lbl_installment_count_result)
        GUITracker.set("personal_info_lbl_total_payment_result", self.lbl_total_payment_result)

        GUITracker.set("personal_info_lbl_starting_date_result", self.lbl_starting_date_result)
        GUITracker.set("personal_info_lbl_ending_date_result", self.lbl_ending_date_result)
        GUITracker.set("personal_info_lbl_loan_count_result", self.lbl_loan_count_result)
        GUITracker.set("personal_info_lbl_work_status_result", self.lbl_work_status_result)

        GUITracker.set("personal_info_btn_report", self.btn_report)

    def locate_components(self):
        GUIUtil.divide_container_equally(self, 5, 24)
        
        # first row
        self.lbl_loan_recipient.grid(row=0, column=0, columnspan=2, sticky="w")
        self.lbl_loan_recipient_result.grid(row=0, column=2, columnspan=4, sticky="w")
        self.lbl_employee_id.grid(row=0, column=6, columnspan=2, sticky="w")
        self.lbl_employee_id_result.grid(row=0, column=8, columnspan=4, sticky="w")
        self.lbl_national_id.grid(row=0, column=12, columnspan=2, sticky="w")
        self.lbl_national_id_result.grid(row=0, column=14, columnspan=4, sticky="w")
        self.lbl_general_status.grid(row=0, column=18, columnspan=2, sticky="w")
        self.lbl_general_status_result.grid(row=0, column=20, columnspan=4, sticky="w")

        # second row
        self.lbl_bank.grid(row=1, column=0, columnspan=2, sticky="w")
        self.lbl_bank_result.grid(row=1, column=2, columnspan=4, sticky="w")
        self.lbl_branch.grid(row=1, column=6, columnspan=2, sticky="w")
        self.lbl_branch_result.grid(row=1, column=8, columnspan=4, sticky="w")
        self.lbl_loan_amount.grid(row=1, column=12, columnspan=2, sticky="w")
        self.lbl_loan_amount_result.grid(row=1, column=14, columnspan=4, sticky="w")
        self.lbl_installment_amount.grid(row=1, column=18, columnspan=2, sticky="w")
        self.lbl_installment_amount_result.grid(row=1, column=20, columnspan=4, sticky="w")
        
        # third row
        self.lbl_account_number.grid(row=2, column=0, columnspan=2, sticky="w")
        self.lbl_account_number_result.grid(row=2, column=2, columnspan=4, sticky="w")
        self.lbl_file_number.grid(row=2, column=6, columnspan=2, sticky="w")
        self.lbl_file_number_result.grid(row=2, column=8, columnspan=4, sticky="w")
        self.lbl_installment_count.grid(row=2, column=12, columnspan=2, sticky="w")
        self.lbl_installment_count_result.grid(row=2, column=14, columnspan=4, sticky="w")
        self.lbl_total_payment.grid(row=2, column=18, columnspan=2, sticky="w")
        self.lbl_total_payment_result.grid(row=2, column=20, columnspan=4, sticky="w")
        
        # fourth row
        self.lbl_starting_date.grid(row=3, column=0, columnspan=2, sticky="w")
        self.lbl_starting_date_result.grid(row=3, column=2, columnspan=4, sticky="w")
        self.lbl_ending_date.grid(row=3, column=6, columnspan=2, sticky="w")
        self.lbl_ending_date_result.grid(row=3, column=8, columnspan=4, sticky="w")
        self.lbl_loan_count.grid(row=3, column=12, columnspan=2, sticky="w")
        self.lbl_loan_count_result.grid(row=3, column=14, columnspan=4, sticky="w")
        self.lbl_work_status.grid(row=3, column=18, columnspan=2, sticky="w")
        self.lbl_work_status_result.grid(row=3, column=20, columnspan=4, sticky="w")

        # fifth row
        self.btn_report.grid(row=4, column=0, columnspan=24, sticky="we")

        
