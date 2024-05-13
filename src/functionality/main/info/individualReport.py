from src.datatbase.dbQuery import DBQuery
from src.functionality.main.info.selectedBorrower import SelectedBorrower
from src.functionality.util.periodUtil import PeriodUtil
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.constants.resourcePath.reportPath import ReportPath
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.excelUtil.excelFileOpening import ExcelFileOpening


class IndividualReport:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate(cls):

        employee_id = SelectedBorrower.get()

        if employee_id is None:
            MessageUtil.show_message(2, "Please first select a user.")
            return "break"

        data, residue = cls.DataRetrieval.retrieve(employee_id)
        processed_data = cls.DataProcess.process(data)
        wb = cls.ExcelFile.generate_file(processed_data, residue)
        cls.FileFormat.format(wb)
        cls.ReportDisplay.display(wb)
        return "break"

    class DataRetrieval:

        @staticmethod
        def retrieve_data(employee_id):
            query_string = f"""
                            SELECT
                            period,
                            comptroller_req, 
                            retires_req,
                            insurance_req,
                            overdue_res,
                            comptroller_res, 
                            retires_res,
                            insurance_res,
                            bank_list,
                            other
                            FROM Saman_Monthly_Data_Data
                            WHERE employee_id = {employee_id}
                            ORDER BY period ASC;
                            """
            result = DBQuery.dql_query(query_string)
            return result

        @staticmethod
        def retrieve_residue(employee_id):
            """returns residue for the given employee_id, in case of failure returns None """

            query_string = f"""
                                    SELECT residue FROM Saman_Residue WHERE employee_id = {employee_id}
                                    """
            result = DBQuery.dql_query(query_string)
            if result:
                return result[0][0]
            else:
                return None

        @classmethod
        def retrieve(cls, employee_id):

            data = cls.retrieve_data(employee_id)
            residue = cls.retrieve_residue(employee_id)
            return [data, residue]
    class DataProcess:
        """
        *** assumptions: ***
        1. data is fetched in order of period
        2. data row order, request, response, bank

        Road Map with an example:
        from data [(140001, data), (140003, data)]
        to [[140001, all-None], [140002, all-None], [140003, all-None]]
        and then [[140001, data], [140002, all-None], [140003, data]] >> wrong
        """

        @staticmethod
        def get_starting_period(data):
            """returns the starting period of the data"""

            return data[0][0]

        @staticmethod
        def get_ending_period(data):
            """returns the ending period of data"""

            return data[-1][0]

        @staticmethod
        def default_report_data(starting_period, ending_period):
            """creates a table with 10 columns, columns 1 is list of periods ( from starting to ending)
                the other columns are just None, to be filled later
            """

            report_period_count = PeriodUtil.period_subtract(ending_period, starting_period) + 1
            default_report_data = []
            period = starting_period

            for i in range(0, report_period_count):
                default_report_data.append([period]+[None]*9)
                period = PeriodUtil.next_month_int(period)

            return default_report_data

        @classmethod
        def complete_report_data(cls, default_data, data):
            """"""
            starting_period = cls.get_starting_period(data)

            for data_row in data:
                data_period = data_row[0]
                idx = PeriodUtil.period_subtract(data_period, starting_period)
                default_data[idx] = list(data_row)

            return default_data

        @staticmethod
        def make_report(complete_report_data):
            report_data = [[None]*10]

            for data_row in complete_report_data:
                # response and banks
                report_data[-1][0] = PeriodUtil.previous_month_int(data_row[0])
                report_data[-1][5:10] = data_row[5:10]
                # request
                data_row[5:10] = [None]*5
                report_data.append(data_row)

            return report_data

        @classmethod
        def process(cls, data):

            if not data:  # no data
                return None
            else:
                starting_period = cls.get_starting_period(data)
                ending_period = cls.get_ending_period(data)
                default_data = cls.default_report_data(starting_period, ending_period)
                complete_data = cls.complete_report_data(default_data, data)
                report_data = cls.make_report(complete_data)
                return report_data

    class ExcelFile:
        @staticmethod
        def write_header(ws):
            """writing headers to given worksheet"""

            header_list = ["دوره", "ارسالی ذی‌حسابی", "ارسالی پایان‌خدمت", "ارسالی بیمه", "معوقات"
                      , "بازخورد ذی‌حسابی", "بازخورد بازنشستگان", "بازخورد بیمه", "ارسالی به بانک", "ارسالی غیره"]

            OpenpyxlUtil.write_header(ws, header_list)

        @staticmethod
        def write_residue(ws, residue):
            """writing residue"""

            ws["A2"] = "باقی‌مانده"
            ws["B2"] = residue

        @staticmethod
        def write_data(ws, data):
            """writing data to given worksheet"""

            for data_row in reversed(data):  # Note it is reversed
                ws.append(data_row)

        @classmethod
        def generate_file(cls, data, residue):
            """generate the monthly report for the given period with the given data"""

            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws)
            cls.write_residue(ws, residue)
            cls.write_data(ws, data)
            return wb

    class FileFormat:

        @staticmethod
        def format(wb):
            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_cell_color(ws["A2"], "86e3b3")
            OpenpyxlUtil.format_cell_color(ws["B2"], "86e3b3")
            OpenpyxlUtil.format_column_width(ws, [("A", "J", 16)])
            column_list = [chr(65 + i - 1) for i in range(2, 11)]
            OpenpyxlUtil.format_column_comma_separated(ws, column_list, starting_row=2)

    class ReportDisplay:

        @staticmethod
        def display(wb):
            """given the wb it saves it and open it then open it"""

            try:
                wb.save(ReportPath.path.value)
                ExcelFileOpening.open(ReportPath.path.value)
            except PermissionError:
                MessageUtil.show_message(2, "Make sure no other report.xlsx file is opened.")




