from src.gui.guiTracking.guiTracker import GUITracker
from src.datatbase.dbQuery import DBQuery
from src.functionality.util.excelUtil.openpyxlUtil import OpenpyxlUtil
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk


class FullReport:

    @classmethod
    @run_func_disp_err_ret_brk
    def generate_report(cls):
        selected_items = cls.ItemSelection.get_selected_items()

        if not selected_items:
            MessageUtil.show_message(2, "One item at least must be selected.")
            return "break"

        selected_borrowers = cls.BorrowerSelection.get_selection()
        data = cls.DataRetrieval.retrieve(selected_items, selected_borrowers)
        wb = cls.ExcelFile.generate(data, selected_items)
        cls.FormatFile.format(wb, selected_items)
        CommonUtil.save_file(wb, "full_report")
        return "break"

    class ItemSelection:

        # column names correspondent to each checkbutton, in DB view column names are set based on this list
        list_of_column_name = [
            "employee_id",
            "national_id",
            "first_name",
            "last_name",
            "residue",

            "general_status",
            "work_status",
            "loan_amount",
            "installment_amount",
            "file_number"
        ]

        @staticmethod
        def get_list_of_widgets():
            """returns the list of checkbutton in their order of appearance"""

            lst = [
                GUITracker.get("batch_operation_full_report_chb_var_employee_id"),
                GUITracker.get("batch_operation_full_report_chb_var_national_id"),
                GUITracker.get("batch_operation_full_report_chb_var_first_name"),
                GUITracker.get("batch_operation_full_report_chb_var_last_name"),
                GUITracker.get("batch_operation_full_report_chb_var_residue"),

                GUITracker.get("batch_operation_full_report_chb_var_general_status"),
                GUITracker.get("batch_operation_full_report_chb_var_work_status"),
                GUITracker.get("batch_operation_full_report_chb_var_loan_amount"),
                GUITracker.get("batch_operation_full_report_chb_var_installment_amount"),
                GUITracker.get("batch_operation_full_report_chb_var_file_number")
            ]
            return lst

        @classmethod
        def get_selected_items(cls):
            """returns a list of corresponding DB column names base on selected item by user"""

            widget_list = cls.get_list_of_widgets()
            column_list = cls.list_of_column_name

            lst = []

            for idx, w in enumerate(widget_list):
                if w.get() == 1:
                    lst.append(column_list[idx])

            return lst

    class BorrowerSelection:
        @staticmethod
        def read_search_bar():
            """return content of search bar entry"""

            ent_search_bar = GUITracker.get("batch_operation_full_report_ent_search_bar")
            search_bar_input = GUIUtil.read_entry(ent_search_bar)
            return search_bar_input

        @classmethod
        def get_selection(cls):
            """returns a list of borrowers or None """

            search_bar_input = cls.read_search_bar()

            if search_bar_input == "" or search_bar_input == " ":
                return None
            else:
                borrower_list = [x.strip() for x in search_bar_input.split(",")]
                return borrower_list

    class DataRetrieval:

        @staticmethod
        def get_query_string(item_list, borrower_list):
            """provides the proper query based on given list of borrowers and items"""

            if borrower_list is None:
                query_string = f"""
                                SELECT {",".join(item_list)} FROM vw_Saman_full_report;
                                """
            else:
                query_string = f"""
                                SELECT {",".join(item_list)} FROM vw_Saman_full_report
                                WHERE employee_id IN ({",".join(borrower_list)});
                                """
            return query_string

        @classmethod
        def retrieve(cls, item_list, borrower_list):
            """retrieve corresponding data of given items from DB for the given borrowers, if no borrower were given
                retrieve the data of all borrowers
            """

            query_string = cls.get_query_string(item_list, borrower_list)
            result = DBQuery.dql_query(query_string)
            return result

    class ExcelFile:
        persian_header_dict = {
            "employee_id": "کد حقوقی",
            "national_id": "کد ملی",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "residue": "باقی مانده",

            "general_status": "وضعیت کلی",
            "work_status": "وضعیت کاری",
            "loan_amount": "مبلغ وام",
            "installment_amount": "مبلغ قسط",
            "file_number": "شماره پرونده"
        }

        @classmethod
        def get_persian_column_name(cls, selected_column_list):
            lst = []
            for c in selected_column_list:
                lst.append(cls.persian_header_dict[c])
            return lst

        @classmethod
        def write_header(cls, ws, selected_column_list):
            """writing headers to given worksheet"""

            header_list = cls.get_persian_column_name(selected_column_list)

            OpenpyxlUtil.write_header(ws, header_list)

        @classmethod
        def generate(cls, data, selected_column_list):
            """generate the monthly report for the given period with the given data"""

            wb = OpenpyxlUtil.get_new_wb()
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            cls.write_header(ws, selected_column_list)
            OpenpyxlUtil.write_data(ws, data)
            OpenpyxlUtil.set_sheet_name(ws, "گزارش کلی")
            return wb

    class FormatFile:
        list_of_comma_separated_column = [
            "residue",
            "loan_amount",
            "installment_amount"
        ]

        @classmethod
        def comma_separated_column_list(cls, item_list):
            """given the list of items selected by user returns alphabetical name of Excel columns which need
                to have comma separated format"""

            idx_lst = []
            for idx, c in enumerate(item_list):
                if c in cls.list_of_comma_separated_column:
                    idx_lst.append(idx)
            column_list = [chr(65+i) for i in idx_lst]
            return column_list

        @classmethod
        def format(cls, wb, selected_column_list):
            OpenpyxlUtil.format_rtl_ws(*wb.worksheets)
            ws = OpenpyxlUtil.return_ws_by_index(wb, 0)
            OpenpyxlUtil.format_global_top_row(ws)
            OpenpyxlUtil.format_column_width(ws, [(f"{chr(65)}", f"{chr(65+len(selected_column_list)-1)}", 18)])
            comma_separated_list = cls.comma_separated_column_list(selected_column_list)
            if comma_separated_list:
                OpenpyxlUtil.format_column_comma_separated(ws, comma_separated_list, starting_row=2)


