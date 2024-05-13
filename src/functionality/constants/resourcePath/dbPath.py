import sys
import os
from enum import Enum


class DBPath(Enum):

    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys._MEIPASS + "\\src\\resource\\database\\deductions_db.db")
    else:
        path = os.path.abspath("resource\\database\\deductions_db.db")

