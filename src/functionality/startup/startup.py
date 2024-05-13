from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.startup.section.monthlyCalculation import MonthlyCalculation
from src.functionality.startup.section.monthlyData import MonthlyData
from src.functionality.startup.section.backup import Backup


class Startup:

    @staticmethod
    @run_func_disp_err_ret_brk
    def initialize():
        """all the actions that should be done when the app start up"""

        MonthlyCalculation.initialize()
        MonthlyData.initialize()
        Backup.initialize()
