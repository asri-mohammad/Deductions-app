from src.datatbase.dbQuery import DBQuery
from src.datatbase.dbUtil import DataRetrieval
from src.functionality.constants.constants import GeneralStatusEnum
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.util.exception.invalidResidue import InvalidActivUserResidue
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil
from src.functionality.main.monthlyCalculation.request.requestComptrollerRetires import RequestComptrollerRetires


class ComptrollerRequest(RequestComptrollerRetires):

    class DataRetrieval(DataRetrieval):

        query_string = """SELECT employee_id, installment_amount, overdue_res, general_status, residue
                          FROM vw_Saman_Comptroller_Request"""

    class DataProcess:

        """In two steps:
            1 . from [employee_id, installment_amount, overdue_res, general_status, residue] to
                [employee_id, residue, request_amount, paycheck_code]
            2. adding bank_code and period """

        class PartiallyProcess:

            @staticmethod
            def not_considering_residue(employee_id, installment_amount, overdue_res, residue):
                """calculating amount and paycheck code without factoring in residue"""

                amount = installment_amount + overdue_res
                return [employee_id, residue, amount, 7]

            @staticmethod
            def considering_residue(employee_id, installment_amount, overdue_res, residue):
                """calculating amount and paycheck code with factoring in residue"""

                if residue is None:  # if residue for an active user is not set in DB
                    raise InvalidActivUserResidue()

                if installment_amount + overdue_res <= residue:
                    amount = installment_amount + overdue_res
                else:
                    if overdue_res > residue:  # if residue is in sync with bank this should not happen
                        amount = overdue_res
                    else:
                        amount = residue

                return [employee_id, residue, amount, 7]

            @classmethod
            def calculate_amount_code(cls, data_row, flag_residue):
                """calculating request amount and paycheck code"""

                employee_id, installment_amount, overdue_res, general_status, residue = data_row

                if general_status != GeneralStatusEnum.active.value:  # DB view contains non active users
                    return [employee_id, residue, 0, 5]

                if flag_residue:  # factoring in residue in calculation
                    return cls.considering_residue(employee_id, installment_amount, overdue_res, residue)
                else:
                    return cls.not_considering_residue(employee_id, installment_amount, overdue_res, residue)

        class ProcessCompletion:

            @staticmethod
            def return_bank_sub_code(bank_name):
                """return the sub code defined for each four banks for the given bank"""

                query_string = f'SELECT sub_code FROM Bank_Sub_Code WHERE bank_name = "{bank_name}"'
                query_result = DBQuery.dql_query(query_string)[0][0]
                return query_result

            @staticmethod
            def add_constants(partially_processed_row, bank_sub_code, period):
                """"""

                employee_id, residue, amount, paycheck_code = partially_processed_row
                return [employee_id, 10, bank_sub_code, period, residue, amount, 0, paycheck_code]

        @classmethod
        def get_generator(cls, data, flag_residue):
            """given raw data and a flag, indicating should residue be factored in calculation or not, returns
                fully completed final row, ready to be written in file"""

            bank_code = cls.ProcessCompletion.return_bank_sub_code("saman")
            period = MonthlyCalcUtil.get_period(output_type="int")

            for row in data:
                partially_processed = cls.PartiallyProcess.calculate_amount_code(row, flag_residue)
                fully_processed = cls.ProcessCompletion.add_constants(partially_processed, bank_code, period)
                yield fully_processed

        @classmethod
        def process(cls, data, flag_residue):
            """returns a generator of fully processed, ready to write in file, data"""

            return cls.get_generator(data, flag_residue)

    class RowColoring(RequestComptrollerRetires.RowColoring):

        @classmethod
        def what_is_color_flag(cls, raw_data_row):
            """given (employee_id, installment_amount, overdue_res, general_status, residue) decides row
             should be colored"""

            employee_id, installment_amount, overdue_res, general_status, residue = raw_data_row
            if (installment_amount + overdue_res > residue) and (general_status == GeneralStatusEnum.active.value):
                return True
            else:
                return False

    class ExcelFile:

        @staticmethod
        def write_header(ws):
            """writes f1, ... , f8 for header"""

            header_list = [f"f{i}" for i in range(1, 9)]
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
                    for j in range(1, 9):
                        OpenpyxlUtil.format_cell_color(ws.cell(i + 2, j), "58d68d")

        @classmethod
        def format(cls, wb, color_flag_list):
            """formatting the given workbook"""

            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [("A", "A", 18), ("B", "D", 10), ("E", "F", 18), ("G", "H", 10)])
            OpenpyxlUtil.format_column_comma_separated(ws, ["E", "F"])

            # coloring rows where installment_amount + overdue < residue
            cls.color(ws, color_flag_list)

    class FileName:

        @staticmethod
        def get():
            """the name of the comptroller request list file  name according to the selected period"""

            period = MonthlyCalcUtil.get_period()
            name = f"{period}_saman_ersali_zihesabi"
            return name
