from abc import ABC, abstractmethod

from tkinter.messagebox import askyesnocancel
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.commonUtil import CommonUtil


class RequestComptrollerRetires:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """generate request list Excel and save it in the user selected directory"""

        flag_residue = RequestComptrollerRetires.ResidueConsideration.ask()

        if flag_residue is None:  # cancel button
            return "break"

        raw_data = cls.DataRetrieval.retrieve()
        processed_data = cls.DataProcess.process(raw_data, flag_residue)
        flag_color_list = cls.RowColoring.get_flag_list(raw_data)
        wb = cls.ExcelFile.generate(processed_data)
        cls.FormatFile.format(wb, flag_color_list)
        wb_name = cls.FileName.get()
        CommonUtil.save_file(wb, wb_name)
        return "break"

    class ResidueConsideration:
        @staticmethod
        def ask():
            """ask the user if they want to factor in residue in their calculation or not"""

            result = askyesnocancel("Residue", "Should residue be factored in calculation?")
            return result

    class RowColoring(ABC):

        @classmethod
        @abstractmethod
        def what_is_color_flag(cls, raw_data_row):
            """given (employee_id, installment_amount, overdue_res, general_status, residue) decides row
             should be colored"""

            pass

        @classmethod
        def get_flag_list(cls, data):
            """given data returns a binary list indicating which rows should be colored"""

            lst = []

            for row in data:
                lst.append(cls.what_is_color_flag(row))

            return lst


