import math

from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.retirementUtils.retirementDivision.fileSaving import FileSaving
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading


class CalcSecFunc:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """command that does the calculation"""

        input_path = cls.InputFile.get_path()

        data = cls.FileDataRetrieval.retrieve(input_path)

        main_processed, banks_processed_list = cls.DataProcess.process(data)

        wb = cls.ExcelFile.generate(main_processed, banks_processed_list)

        cls.FormatFile.format(wb)

        FileSaving.set_current_file(wb)

        cls.InfoMessage.display("Calculation is done.")

    class InfoMessage:

        @staticmethod
        def display(msg):
            msg_entry = GUITracker.get("division_txt_info")
            GUIUtil.clear_write_text_widget(msg_entry, msg)

    class InputFile:

        @staticmethod
        def get_path():
            """from entry reads the selected file path and returns it"""

            path = GUITracker.get("division_ent_filePath").get()
            return path

    class FileDataRetrieval:

        @staticmethod
        def retrieve(file_path):
            data = ExcelDataReading.read(file_path, 7)
            return data

    class DataProcess:
        
        class MainProcess:
            
            @staticmethod
            def none_to_zero(lst):
                """changes all None values in the list to zero"""
                new_lst = [0 if x is None else x for x in lst]
                return new_lst
            
            @classmethod
            def division(cls, data_lst):
                """given a list of size (sr, mr, rr, tr, b) returns a list of 4 including final result (s, m, r, t)"""
                # b = bazkhord, r = requested
                
                sr_idx, mr_idx, rr_idx, tr_idx, b = range(0, 5)

                data_lst = cls.none_to_zero(data_lst)

                if data_lst[b] == 0:
                    return [0] * 4
                elif sum(data_lst[sr_idx: b]) <= data_lst[b]:
                    return data_lst[sr_idx: b]
                else:
                    result = [0] * 4
                    reminder = data_lst[b]
                    for i in range(0, 4):
                        if reminder < data_lst[i]:
                            result[i] = math.floor(reminder)
                            break
                        else:
                            result[i] = data_lst[i]
                            reminder = reminder - data_lst[i]
                    return result
            
            @classmethod
            def process(cls, data):
                """given the datat returns [data, divided data]"""
                
                processed_data = []
                
                for row in data:
                    row = list(row)
                    result_lst = cls.division(row[2:7])
                    processed_data.append([*row, *result_lst])

                return processed_data

        class SecondaryProcess:
            
            @staticmethod
            def process(main_processed_data):
                """returns a list of 4 lists, each containing non-zero values for each bank"""
                
                saman, maskan, resalat, tejarat = [], [], [], []

                s_idx, m_idx, r_idx, t_idx, salary_code_idx = 7, 8, 9, 10, 0

                for row in main_processed_data:
                    if row[s_idx] != 0:
                        saman.append([row[salary_code_idx], row[s_idx]])
                    if row[m_idx] != 0:
                        maskan.append([row[salary_code_idx], row[m_idx]])
                    if row[r_idx] != 0:
                        resalat.append([row[salary_code_idx], row[r_idx]])
                    if row[t_idx] != 0:
                        tejarat.append([row[salary_code_idx], row[t_idx]])

                return [saman, maskan, resalat, tejarat]

        @classmethod
        def process(cls, data):

            main_processed_data = cls.MainProcess.process(data)

            banks_processed_data_list  = cls.SecondaryProcess.process(main_processed_data)

            return [main_processed_data, banks_processed_data_list]

    class ExcelFile:
        
        @staticmethod
        def generate_main(ws, data):
            
            header_list = ["شماره حقوقی", "دلخواه", "درخواستی سامان", "درخواستی مسکن", "درخواستی رسالت",
                           "درخواستی تجارت", "بازخورد", "سامان", "مسکن", "رسالت", "تجارت"]
            OpenpyxlUtil.write_header(ws, header_list)
            OpenpyxlUtil.write_data(ws, data)
            
        @staticmethod
        def generate_four_banks(ws_list, data_list):
            
            per_bank_header = ["کد حقوقی", "مبلغ"]
            
            for i in range(0, 4):
                OpenpyxlUtil.write_header(ws_list[i], per_bank_header)
                OpenpyxlUtil.write_data(ws_list[i], data_list[i])
                
        @staticmethod
        def generate_total_sum(ws, max_row):
            ws["A1"] = "بانک"
            ws["A2"] = "سامان"
            ws["A3"] = "مسکن"
            ws["A4"] = "رسالت"
            ws["A5"] = "تجارت"
            ws["A6"] = "جمع"

            ws["B1"] = "جمع کل"

            ws["B2"] = "=sum(محاسبه!H2:H" + str(max_row) + ")"
            ws["B3"] = "=sum(محاسبه!I2:I" + str(max_row) + ")"
            ws["B4"] = "=sum(محاسبه!J2:J" + str(max_row) + ")"
            ws["B5"] = "=sum(محاسبه!K2:K" + str(max_row) + ")"
            ws["B6"] = "=SUM(B2:B5)"
            
        @classmethod
        def generate(cls, main_data, banks_data_list):

            wb = OpenpyxlUtil.get_new_wb()

            wb.active.title = "محاسبه"
            wb.create_sheet("جمع کل")
            wb.create_sheet("سامان")
            wb.create_sheet("مسکن")
            wb.create_sheet("رسالت")
            wb.create_sheet("تجارت")

            cls.generate_main(wb["محاسبه"], main_data)

            max_row = len(main_data) + 2
            cls.generate_total_sum(wb["جمع کل"], max_row)

            ws_list = [wb["سامان"], wb["مسکن"], wb["رسالت"], wb["تجارت"]]
            cls.generate_four_banks(ws_list, banks_data_list)

            return wb

    class FormatFile:

        @staticmethod
        def format_calculation_ws(ws):
            OpenpyxlUtil.format_column_width(ws, [("A", "K", 15)])

        @staticmethod
        def format_total_sum_ws(ws):
            OpenpyxlUtil.format_column_width(ws, [("B", "B", 15)])

        @staticmethod
        def format_per_bank_wss(*worksheets):
            for ws in worksheets:
                OpenpyxlUtil.format_column_width(ws, [("A", "B", 15)])

        @staticmethod
        def format_headers(wb):
            """set a header format for top row of each sheet in the workbook"""
            for ws in wb.worksheets:
                OpenpyxlUtil.format_global_top_row(ws)

        @classmethod
        def format(cls, wb):
            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            cls.format_headers(wb)
            cls.format_calculation_ws(wb["محاسبه"])
            cls.format_total_sum_ws(wb["جمع کل"])
            cls.format_per_bank_wss(wb["سامان"], wb["مسکن"], wb["رسالت"], wb["تجارت"])



