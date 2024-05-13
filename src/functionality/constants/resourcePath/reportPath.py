import sys
import os
from enum import Enum


class ReportPath(Enum):

    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys._MEIPASS + "\\src\\resource\\report\\report.xlsx")
    else:
        path = os.path.abspath(os.getcwd()+"\\resource\\report\\report.xlsx")

