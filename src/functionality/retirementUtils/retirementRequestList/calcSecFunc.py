# from openpyxl.workbook import Workbook
#
# from src.gui.guiTracking.guiTracker import GUITracker
# from src.functionality.util.guiUtil import GUIUtil
# from src.functionality.util.commonUtil import CommonUtil
# from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
# from src.functionality.retirementUtils.retirementRequestList.saveSecFunc import SaveSecFunc
# from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
# from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
#
#
# class CalcSecFunc:
#
#     # ent_file_path = None
#     # txt_info = None
#     #
#     # @classmethod
#     # def show_message(cls, message):
#     #     """display the given message in the text widget of info section"""
#     #     GUIUtil.clear_write_text_widget(cls.txt_info, message)
#     #
#     # @classmethod
#     # def read_file_path(cls):
#     #     """returns the file path in the entry widget"""
#     #     path = GUIUtil.read_entry(cls.ent_file_path)
#     #     return path
#     #
#     # @staticmethod
#     # def check_file_path(path):
#     #     """check if the provided file path is ok"""
#     #     return CommonUtil.check_file_exist(path)
#     #
#     # @staticmethod
#     # def open_file(path):
#     #     """returning the workbook for the given path"""
#     #     wb = OpenpyxlUtil.load_excel_file(path, True)
#     #     return wb
#     #
#     # @staticmethod
#     # def check_wb_format(wb):
#     #     """checking the workbook format"""
#     #     return True
#     #
#     # @staticmethod
#     # def check_ws_format(ws):
#     #     """checking the sheet format"""
#     #     return True
#     #
#     # @staticmethod
#     # def calculation(ws):
#     #     """
#     #     doing the real calculation in the given worksheet (containing the data) and returns a workbook containing
#     #     the final result
#     #     """
#     #     return Calculation().calculate(ws)
#     #
#     # @staticmethod
#     # def format(wb):
#     #     Format.format(wb)
#
#     @classmethod
#     @run_func_disp_err_ret_brk
#     def generate(cls):
#         """command that does the calculation"""
#
#         input_path = cls.InputFile.get_path()
#
#         data = cls.FileDataRetrieval.retrieve(input_path)
#
#         processed_data = cls.DataProcess.process(data)
#
#         wb = cls.ExcelFile.generate(processed_data)
#
#         cls.FormatFile.format(wb)
#
#         FileSaving.set_current_file(wb)
#
#         cls.InfoMessage.display("Calculation is done.")
#
#     class InfoMessage:
#
#         @staticmethod
#         def display(msg):
#             msg_entry = GUITracker.get("retirement_request_txt_info")
#             GUIUtil.clear_write_text_widget(msg_entry, msg)
#
#     class InputFile:
#
#         @staticmethod
#         def get_path():
#             """from entry reads the selected file path and returns it"""
#
#             path = GUITracker.get("retirement_request_ent_filePath").get()
#             return path
#
#     class FileDataRetrieval:
#
#         @staticmethod
#         def retrieve(file_path):
#             data = ExcelDataReading.read(file_path, 8)
#             return data
#
#     class DataProcess:
#         @staticmethod
#         def unique_employee_number(data):
#             """return a set of unique employee numbers from 4 bank lists that has at least one non-zero value"""
#
#             employee_number_set = set()
#
#             for row in data:
#                 row = list(row)
#                 for i in range(0, 8, 2):
#                     if (row[i] is not None) and (row[i + 1] != 0):
#                         employee_number_set.add(row[i])
#
#             return employee_number_set
#
#         @staticmethod
#         def retirement_request_dict(employee_number_set, data):
#             """returns a dictionary withe key:pair as follows employeeNum: [saman, maskan, resalat, tejarat]"""
#
#             result_dict = {}
#
#             for employee_num in employee_number_set:
#                 result_dict[employee_num] = [0, 0, 0, 0]
#
#             for row in data:
#                 row = list(row)
#                 for i in range(0, 8, 2):
#                     if (row[i] is not None) and (row[i + 1] != 0):
#                         result_dict[row[i]][i // 2] = row[i + 1]
#
#             return result_dict
#
#         @classmethod
#         def process(cls, data):
#             """ reading data from source ws and writing the output result in the destination ws"""
#
#             employee_number_set = cls.unique_employee_number(data)
#             result_dict = cls.retirement_request_dict(employee_number_set, data)
#
#             result = []
#
#             counter = 2
#             for key, value in result_dict.items():
#                 result.append([key] + value + [f"=sum(B{counter}:E{counter})"])
#                 counter += 1
#
#             return result
#
#     class ExcelFile:
#
#         @staticmethod
#         def write_header(ws):
#
#             header_list = ["کد حقوقی", "سامان", "مسکن", "رسالت", "تجارت", "مجموع"]
#             OpenpyxlUtil.write_header(ws, header_list)
#         @classmethod
#         def generate(cls, data):
#             wb = OpenpyxlUtil.get_new_wb()
#             ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
#             cls.write_header(ws)
#             OpenpyxlUtil.write_data(ws, data)
#             return wb
#
#     class FormatFile:
#         @staticmethod
#         def format(wb):
#
#             OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
#             ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
#             OpenpyxlUtil.format_global_top_row(ws)
#             OpenpyxlUtil.format_column_width(ws, [("A", "F", 18)])
#             OpenpyxlUtil.format_column_comma_separated(ws, ["B", "C", "D", "E", "F"], starting_row=2)
#
#
# class Calculation:
#
#     # @staticmethod
#     # def unique_employee_number(source_ws):
#     #     """return a set of unique employee numbers from 4 bank lists that has at least one non-zero value"""
#     #     employee_number_set = set()
#     #
#     #     for row in source_ws.iter_rows(min_row=2, min_col=1, max_col=8):
#     #         row_value = [c.value for c in row]
#     #         for i in range(0, 8, 2):
#     #             if (row_value[i] is not None) and (row_value[i+1] != 0):
#     #                 employee_number_set.add(row_value[i])
#     #
#     #     return employee_number_set
#
#     # @staticmethod
#     # def retirement_request_dict(employee_number_set, source_ws):
#     #     """returns a dictionary withe key:pair as follows employeeNum: [saman, maskan, resalat, tejarat]"""
#     #     result_dict = {}
#     #
#     #     for employee_num in employee_number_set:
#     #         result_dict[employee_num] = [0, 0, 0, 0]
#     #
#     #     for row in source_ws.iter_rows(min_row=2, min_col=1, max_col=8):
#     #         row_value = [c.value for c in row]
#     #         for i in range(0, 8, 2):
#     #             if (row_value[i] is not None) and (row_value[i+1] != 0):
#     #                 result_dict[row_value[i]][i//2] = row_value[i+1]
#     #
#     #     return result_dict
#
#     # @staticmethod
# #     def write_result_dict_to_sheet(result_dict, destination_ws):
# #         destination_ws.append(["کد حقوقی", "سامان", "مسکن", "رسالت", "تجارت", "مجموع"])
# #         counter = 2
# #         for key, value in result_dict.items():
# #             destination_ws.append([key] + value + [f"=sum(B{counter}:E{counter})"])
# #             counter += 1
# #
# #     # def calculate_main_sheet(self, source_ws, destination_ws):
# #     #     """ reading data from source ws and writing the output result in the destination ws
# #     #     """
# #     #     employee_number_set = self.unique_employee_number(source_ws)
# #     #     result_dict = self.retirement_request_dict(employee_number_set, source_ws)
# #     #     self.write_result_dict_to_sheet(result_dict, destination_ws)
# #
# #     def calculate(self, ws):
# #         """ doing the real calculation in the given worksheet (containing the data) and returns a workbook containing
# #             the final result"""
# #         wb = Workbook()
# #         wb.active.title = "ارسالی پایان خدمت"
# #
# #         self.calculate_main_sheet(ws, wb["ارسالی پایان خدمت"])
# #
# #         return wb
# #
# # # ************************************* NEW CLASS *************************************
# #
# #
# # class Format:
# #     @staticmethod
# #     def rtl_worksheets(wb):
# #         OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
# #
# #     @staticmethod
# #     def format_headers(wb):
# #         """set a header format for top row of each sheet in the workbook"""
# #         for ws in wb.worksheets:
# #             OpenpyxlUtil.format_global_top_row(ws)
# #
# #     @staticmethod
# #     def format(wb):
# #         Format.rtl_worksheets(wb)
# #         Format.format_headers(wb)
