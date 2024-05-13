from enum import Enum
import sys
import os


class SamplePath(Enum):
    if getattr(sys, 'frozen', False):
        root_path = os.path.abspath(sys._MEIPASS + "\\src\\resource\\sampleFiles\\")
    else:
        root_path = "resource\\sampleFiles\\"

    bank_letter = os.path.abspath(os.path.join(root_path, "sample_bank_letter.docx"))
    division = os.path.abspath(os.path.join(root_path, "sample_division.xlsx"))
    employee_id_money = os.path.abspath(os.path.join(root_path, "sample_employeeID_moneyAmount.xlsx"))
    national_id_money = os.path.abspath(os.path.join(root_path, "sample_nationalID_moneyAmount.xlsx"))
    retirement_req_list = os.path.abspath(os.path.join(root_path, "sample_retirement_request_list.xlsx"))
    unknown_list = os.path.abspath(os.path.join(root_path, "sample_unknown_list.xlsx"))
    work_status = os.path.abspath(os.path.join(root_path, "sample_update_work_status.xlsx"))
    residue_update = os.path.abspath(os.path.join(root_path, "sample_update_residue.xlsx"))
    general_statu_update = os.path.abspath(os.path.join(root_path, "sample_update_general_status.xlsx"))

