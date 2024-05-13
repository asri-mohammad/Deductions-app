from src.datatbase.dbQuery import DBQuery
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class MonthlyReport:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):

        period = MonthlyDataUtil.get_period(output_type="int")

        data = cls.DataRetrieval.retrieve(period)

        if not data:  # just an empty list
            MessageUtil.show_message(1, "No data is provided for the selected period.")
            return "break"

        wb = cls.ExcelFile.generate(data)
        cls.FormatFile.format(wb)
        wb_name = cls.FileName.get()
        CommonUtil.save_file(wb, wb_name)
        return "break"

    class DataRetrieval:

        @staticmethod
        def retrieve(period):
            """returns either None, if there is no such period in DB Or
              a list like [(employee_id, ...),(employee_id, ...) ]"""

            query_string = f"""
                                            SELECT
                                            Saman_Monthly_Data_Data.employee_id     ,
                                            national_id     ,
                                            first_name      ,
                                            last_name       ,
                                            comptroller_res ,
                                            retires_res     ,
                                            insurance_res   ,
                                            bank_list       ,
                                            other           ,
                                            overdue_res     ,
                                            comptroller_req ,
                                            retires_req     ,
                                            insurance_req
                                            FROM Saman_Monthly_Data_Data
                                            INNER JOIN Saman_Info ON Saman_Monthly_Data_Data.employee_id = Saman_Info.employee_id
                                            WHERE period = {period}
                                            ORDER BY Saman_Monthly_Data_Data.employee_id;
                                        """
            result = DBQuery.dql_query(query_string)

            if result:  # set is not empty
                return result
            else:
                return None

    class ExcelFile:
        @staticmethod
        def write_header(ws):
            """writing headers to given worksheet"""

            header_list = ["کد حقوقی", "کد ملی", "نام", "نام خانوادگی",
                      "بازخورد ذی حسابی", "بازخورد بازنشستگان", "بازخورد بیمه",
                      "ارسالی به بانک", "ارسالی به بانک (غیره) ", "معوقات", "ارسالی ذی حسابی", "ارسالی بازنشستگان ", "ارسالی بیمه"]

            OpenpyxlUtil.write_header(ws, header_list)

        @staticmethod
        def write_total_sum(ws):
            total_sum_row = ws.max_row + 2
            ws[f"A{total_sum_row}"] = "جمع کل"

            for i in range(5, 14):  # column 5 to 13
                ws[f"{chr(65 + i - 1)}{total_sum_row}"] = f"=SUM({chr(65 + i - 1)}2:{chr(65 + i - 1)}{total_sum_row-2})"

        @classmethod
        def generate(cls, data):
            """generate the monthly report for the given period with the given data"""

            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws)
            OpenpyxlUtil.write_data(ws, data)
            cls.write_total_sum(ws)
            return wb

    class FormatFile:
        @staticmethod
        def format(wb):

            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [("A", "M", 18)])
            column_list = [chr(65+i-1) for i in range(5, 14)]
            OpenpyxlUtil.format_column_comma_separated(ws, column_list, starting_row=2)

    class FileName:

        @staticmethod
        def get():
            """returns the file name"""

            period = MonthlyDataUtil.get_period()
            file_name = f"data_of_month_{period}"
            return file_name

