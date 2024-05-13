import sys
import os
from enum import Enum


class InsuranceUpdatePath(Enum):
    if getattr(sys, 'frozen', False):
        root_path = os.path.abspath(sys._MEIPASS + "\\src\\resource\\insuranceUpdate\\")
    else:
        root_path = "resource\\insuranceUpdate\\"

    eligibles = os.path.abspath(os.path.join(root_path, "eligibles.xlsx"))
    reasons = os.path.abspath(os.path.join(root_path, "reasons.xlsx"))
