from src.datatbase.dbQuery import DBQuery
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.constants.constants import GeneralStatusEnum
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading


class UnknownList:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """returns and store an Excel file including employee ids that their status is not provided"""

        data_file_path = GUIUtil.ask_open_file_name()

        if data_file_path == "":  # cancel button
            return "break"

        known_set = cls.KnownBorrower.get_set(data_file_path)
        active_set = cls.ActiveBorrower.get_set()
        unknown_set = cls.UnknownBorrower.get_set(active_set, known_set)
        #  generate function can  only add iterables data rows
        iterable_unknown_set = [(d, ) for d in unknown_set]
        wb = cls.ExcelFile.generate(iterable_unknown_set)
        cls.FormatFile.format(wb)
        CommonUtil.save_file(wb, "unknownList")
        return "break"

    class ActiveBorrower:

        @staticmethod
        def get_set():
            """returns a set of all users with active general status"""

            # TODO: what about temp stops
            query_string = f'SELECT employee_id FROM Saman_General_Status WHERE general_status = {GeneralStatusEnum.active.value}'
            result = DBQuery.dql_query(query_string)  # [(id,), (id2,), ... ]

            active_set = set([r[0] for r in result])

            return active_set

    class KnownBorrower:

        @staticmethod
        def get_set(data_file_path):
            """reads from a file and return a set of employee ids which were in the file"""

            data = ExcelDataReading.read(data_file_path, max_col=1)  # [(id,), (id2,), ... ]

            known_set = set([r[0] for r in data])

            return known_set

    class UnknownBorrower:

        @staticmethod
        def get_set(active_set: set, known_set: set):
            """returns the set of users that their working status are unknown"""

            return active_set.difference(known_set)

    class ExcelFile:

        @staticmethod
        def write_header(ws):
            """writing headers to given worksheet"""

            header_list = ["کد حقوقی"]
            OpenpyxlUtil.write_header(ws, header_list)

        @classmethod
        def generate(cls, data):
            """generating final Excel file with a column with unknown user's employee id"""

            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws)
            OpenpyxlUtil.write_data(ws, data) # data rows must be iterable
            return wb

    class FormatFile:

        @staticmethod
        def format(wb):
            """formats the given workbook"""

            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [("A", "A", 18)])
