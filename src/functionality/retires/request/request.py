from openpyxl.utils.exceptions import InvalidFileException

from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading

from src.functionality.retires.request.fileSaving import FileSaving


class Request:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """command that does the calculation"""

        input_path = cls.InputFile.get_path()

        try:
            data = cls.FileDataRetrieval.retrieve(input_path)
        except InvalidFileException:
            cls.InfoMessage.display("Check the file path.")
            return "break"

        processed_data = cls.DataProcess.process(data)

        wb = cls.ExcelFile.generate(processed_data)

        cls.FormatFile.format(wb)

        FileSaving.set_current_file(wb)

        cls.InfoMessage.display("Calculation is done.")

    class InfoMessage:

        @staticmethod
        def display(msg):
            msg_entry = GUITracker.get("retirement_request_txt_info")
            GUIUtil.clear_write_text_widget(msg_entry, msg)

    class InputFile:

        @staticmethod
        def get_path():
            """from entry reads the selected file path and returns it"""

            path = GUITracker.get("retirement_request_ent_filePath").get()
            return path

    class FileDataRetrieval:

        @staticmethod
        def retrieve(file_path):
            data = ExcelDataReading.read(file_path, 8)
            return data

    class DataProcess:
        @staticmethod
        def unique_employee_number(data):
            """return a set of unique employee numbers from 4 bank lists that has at least one non-zero value"""

            employee_number_set = set()

            for row in data:
                row = list(row)
                for i in range(0, 8, 2):
                    if (row[i] is not None) and (row[i + 1] != 0):
                        employee_number_set.add(row[i])

            return employee_number_set

        @staticmethod
        def retirement_request_dict(employee_number_set, data):
            """returns a dictionary withe key:pair as follows employeeNum: [saman, maskan, resalat, tejarat]"""

            result_dict = {}

            for employee_num in employee_number_set:
                result_dict[employee_num] = [0, 0, 0, 0]

            for row in data:
                row = list(row)
                for i in range(0, 8, 2):
                    if (row[i] is not None) and (row[i + 1] != 0):
                        result_dict[row[i]][i // 2] = row[i + 1]

            return result_dict

        @classmethod
        def process(cls, data):
            """ reading data from source ws and writing the output result in the destination ws"""

            employee_number_set = cls.unique_employee_number(data)
            result_dict = cls.retirement_request_dict(employee_number_set, data)

            result = []

            counter = 2
            for key, value in result_dict.items():
                result.append([key] + value + [f"=sum(B{counter}:E{counter})"])
                counter += 1

            return result

    class ExcelFile:

        @staticmethod
        def write_header(ws):
            header_list = ["کد حقوقی", "سامان", "مسکن", "رسالت", "تجارت", "مجموع"]
            OpenpyxlUtil.write_header(ws, header_list)

        @classmethod
        def generate(cls, data):
            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws)
            OpenpyxlUtil.write_data(ws, data)
            return wb

    class FormatFile:
        @staticmethod
        def format(wb):
            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [("A", "F", 18)])
            OpenpyxlUtil.format_column_comma_separated(ws, ["B", "C", "D", "E", "F"], starting_row=2)
