from src.datatbase.dbUtil import DataRetrieval
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.util.exception.invalidResidue import InvalidActivUserResidue
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil
from src.functionality.main.monthlyCalculation.request.requestComptrollerRetires import RequestComptrollerRetires
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class RetiresRequest(RequestComptrollerRetires):

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """generate request list Excel and save it in the user selected directory"""

        if not MonthlyCalcUtil.work_status_update_state():
            MessageUtil.show_message(2, "First statuses should be updated.")
            return "break"

        super().generate()

    class DataRetrieval(DataRetrieval):

        # DB view only contains vw_Saman_Retires_Request 'active' user with work status 16
        query_string = """SELECT employee_id, installment_amount, overdue_res, residue
                            FROM vw_Saman_Retires_Request"""

    class DataProcess:

        @staticmethod
        def not_considering_residue(data_row):
            """calculating amount and paycheck code without factoring in residue"""

            employee_id, installment_amount, overdue_res, residue = data_row

            amount = installment_amount + overdue_res
            return [employee_id, amount]

        @staticmethod
        def considering_residue(data_row):
            """calculating amount and paycheck code with factoring in residue"""

            employee_id, installment_amount, overdue_res, residue = data_row

            if residue is None:  # if residue for an active user is not set in DB
                raise InvalidActivUserResidue()

            if installment_amount + overdue_res <= residue:
                amount = installment_amount + overdue_res
            else:
                if overdue_res > residue:  # if residue is in sync with bank this should not happen
                    amount = overdue_res
                else:
                    amount = residue

            return [employee_id, amount]

        @classmethod
        def get_generator(cls, data, flag_residue):
            """given raw data and a flag, indicating should residue be factored in calculation or not, returns
                fully completed final row, ready to be written in file"""

            for row in data:
                if flag_residue:
                    yield cls.considering_residue(row)
                else:
                    yield cls.not_considering_residue(row)

        @classmethod
        def process(cls, data, flag_residue):
            """returns a generator of fully processed, ready to write in file, data"""

            return cls.get_generator(data, flag_residue)

    class RowColoring(RequestComptrollerRetires.RowColoring):
        @classmethod
        def what_is_color_flag(cls, raw_data_row):
            """given (employee_id, installment_amount, overdue_res, general_status, residue) decides row
                     should be colored"""

            employee_id, installment_amount, overdue_res, residue = raw_data_row

            if installment_amount + overdue_res > residue:
                return True
            else:
                return False

    class ExcelFile:

        @staticmethod
        def write_header(ws):
            """excel file header"""

            header_list = ["کد حقوقی", "مبلغ درخواستی"]
            OpenpyxlUtil.write_header(ws, header_list)

        @classmethod
        def generate(cls, data):
            """returns the final workbook fully completed"""

            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws)
            OpenpyxlUtil.write_data(ws, data)
            return wb

    class FormatFile:

        @staticmethod
        def color(ws, color_flag_list):
            """given a binary list, colors those rows with 1 value"""

            for i, data_row in enumerate(ws.iter_rows(min_row=2)):
                if color_flag_list[i]:
                    for j in range(1, 3):
                        OpenpyxlUtil.format_cell_color(ws.cell(i+2, j), "58d68d")

        @classmethod
        def format(cls, wb, color_flag_list):
            """formatting the given workbook"""

            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [("A", "B", 18)])
            OpenpyxlUtil.format_column_comma_separated(ws, ["B"])

            # coloring rows where installment_amount + overdue < residue
            cls.color(ws, color_flag_list)

    class FileName:

        @staticmethod
        def get():
            """the name of the comptroller request list file  name according to the selected period"""

            period = MonthlyCalcUtil.get_period()
            name = f"{period}_saman_ersali_payan_khedmat"
            return name