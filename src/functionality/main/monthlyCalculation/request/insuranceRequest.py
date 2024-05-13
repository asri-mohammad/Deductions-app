from src.datatbase.dbUtil import DataRetrieval
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.periodUtil import PeriodUtil
from src.functionality.main.monthlyCalculation.monthlyCalcUtil import MonthlyCalcUtil


class InsuranceRequest:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):
        """generate insurance request list Excel and save it in the user selected directory"""

        if not MonthlyCalcUtil.work_status_update_state():
            MessageUtil.show_message(2, "First statuses should be updated.")
            return "break"

        data = cls.DataRetrieval.retrieve()
        excel_file = cls.ExcelFile.generate(data)
        cls.FormatFile.format(excel_file)
        excel_file_name = cls.FileName.get()
        CommonUtil.save_file(excel_file, excel_file_name)
        return "break"

    class DataRetrieval(DataRetrieval):
        query_string = """SELECT
                        employee_id, national_id, first_name, last_name, unit, residue, 
                        comptroller_req, paid, not_paid, reason
                        FROM vw_Saman_Insurance_Request"""

    class ExcelFile:

        @staticmethod
        def write_header(ws):
            """excel file header"""

            header_list = ["کد حقوقی", "کد ملی", "نام", "نام خانوادگی", "یگان", "مانده وام", "مبلغ قسط", "پرداخت شده", "باقی مانده قسط",
                      "دلیل"]
            OpenpyxlUtil.write_header(ws, header_list)

        @classmethod
        def generate(cls, data):
            """generate insurance request Excel file for given data"""
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
            OpenpyxlUtil.format_column_width(ws, [("A", "D", 15), ("E", "E", 20), ("F", "J", 15)])
            OpenpyxlUtil.format_column_comma_separated(ws, ["G", "H", "I"])
            OpenpyxlUtil.format_column_rtl(ws, ["J"])

    class FileName:

        @classmethod
        def get(cls):
            """returns file name"""

            period = MonthlyCalcUtil.get_period()
            perv_period = PeriodUtil.previous_month_str(period)
            name = f"{perv_period}_saman_ersali_gheramat_bime"
            return name