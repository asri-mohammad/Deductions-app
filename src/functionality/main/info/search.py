from enum import Enum

from src.gui.guiTracking.guiTracker import GUITracker
from src.datatbase.dbQuery import DBQuery
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.commonUtil import CommonUtil
from src.functionality.main.info.selectedBorrower import SelectedBorrower
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.constants.constants import GeneralStatusEnum


class Search:
    
    # represent info DB table column's names
    info_elements = [
        "general_status",
        "registration_date",
        "employee_id",
        "national_id",
        "first_name",
        "last_name",
        "branch_id",
        "customer_id",
        "account_num",
        "file_num",
        "loan_amount",
        "installment_num",
        "installment_amount",
        "loan_count",
        "total_payment",
        "starting_date",
        "ending_date",
        "work_status_id"
                    ]

    @classmethod
    @run_func_disp_err_ret_brk
    def search(cls):
        """reads from search bar and set the values of info section widgets dictionary if user is found"""

        entry_search_bar = GUITracker.get("info_search_ent_search")
        lbl_message_bar = GUITracker.get("info_search_lbl_message")

        searched_string = GUIUtil.read_entry(entry_search_bar)

        query_string = cls.QueryString.get(searched_string)

        borrower_info_dic = cls.BorrowerInfo.get(query_string)

        if borrower_info_dic is None:  # no borrower is found
            lbl_message_bar.config(text="No user has been found, check the search input.")
            cls.InfoDisplay.display_default()
            SelectedBorrower.set_to_none()
            return "break"
        
        else:  # a borrower is found
            cls.InfoDisplay.display_borrower(borrower_info_dic)
            lbl_message_bar.config(text="")
            SelectedBorrower.set(borrower_info_dic["employee_id"])
            return "break"

    class QueryString:

        class SearchType(Enum):
            employee_id = 1,
            national_id = 2,
            name = 3

        @classmethod
        def get_query_type(cls, searched_string):
            """to decide what is the user trying to search base on, employee number, national number, etc"""

            if searched_string.isdigit():
                if len(searched_string) == 10:
                    return cls.SearchType.national_id.value
                else:
                    return cls.SearchType.employee_id.value
            else:
                return cls.SearchType.name.value

        @classmethod
        def get(cls, searched_string):
            """creating right query string based on what user has searched for"""

            searched_string = searched_string.strip()

            query_type = cls.get_query_type(searched_string)

            init_query = f"""SELECT 
                               Saman_General_Status.general_status,
                               Saman_General_Status.registration_date,	
                               Saman_Info.employee_id,
                               Saman_Info.national_id,
                               Saman_Info.first_name,
                               Saman_Info.last_name,
                               Saman_Info.branch_id,
                               Saman_Info.customer_id,
                               Saman_Info.account_num,
                               Saman_Info.file_num,
                               Saman_Info.loan_amount,
                               Saman_Info.installment_num,
                               Saman_Info.installment_amount,
                               Saman_Info.loan_count,
                               Saman_Info.total_payment,
                               Saman_Info.starting_date,
                               Saman_Info.ending_date,
                               Saman_Work_Status.work_status_id
                               FROM Saman_Info
                               INNER JOIN Saman_General_Status ON Saman_General_Status.employee_id=Saman_Info.employee_id
                               INNER JOIN Saman_Work_Status ON Saman_Work_Status.employee_id=Saman_Info.employee_id  
                               WHERE 
                           """

            if query_type == cls.SearchType.national_id.value:
                return init_query + " " + f'Saman_Info.national_id = "{searched_string}";'
            elif query_type == cls.SearchType.employee_id.value:
                return init_query + " " + f"Saman_Info.employee_id = {searched_string};"
            elif query_type == cls.SearchType.name.value:
                return init_query + " " + f'Saman_Info.first_name || " " || Saman_Info.last_name = "{searched_string}" ;'

    class BorrowerInfo:

        @classmethod
        def get(cls, query_string):
            """returns a dictionary representing user data, None if the there was no match for search"""

            query_result = DBQuery.dql_query(query_string)
            if not query_result:  # it is an empty list
                return None
            else:
                user_info_dic = {}
                for i, element in enumerate(Search.info_elements):
                    user_info_dic[element] = query_result[0][i]
                return user_info_dic

    class GeneralStatusDescription:

        @staticmethod
        def general_status_value(status, date):
            status_text = ""
            if status == GeneralStatusEnum.active.value:
                status_text = "Active"
            elif status == GeneralStatusEnum.settled.value:
                status_text = "Settled"
            elif status == GeneralStatusEnum.passed_away.value:
                status_text = "Passed-away"
            elif status == GeneralStatusEnum.temp_stop.value:
                status_text = "temp-stop"

            if date is not None:
                status_text = f"{status_text} {date}"

            return status_text

    class InfoDisplay:
        @staticmethod
        def get_info_widget_dic():

            info_widget_dic = {
                "loan_recipient": GUITracker.get("personal_info_lbl_loan_recipient_result"),
                "employee_id": GUITracker.get("personal_info_lbl_employee_id_result"),
                "national_id": GUITracker.get("personal_info_lbl_national_id_result"),
                "general_status": GUITracker.get("personal_info_lbl_general_status_result"),
                "bank": GUITracker.get("personal_info_lbl_bank_result"),
                "branch": GUITracker.get("personal_info_lbl_branch_result"),
                "loan_amount": GUITracker.get("personal_info_lbl_loan_amount_result"),
                "installment_amount": GUITracker.get("personal_info_lbl_installment_amount_result"),
                "account_number": GUITracker.get("personal_info_lbl_account_number_result"),
                "file_number": GUITracker.get("personal_info_lbl_file_number_result"),
                "installment_count": GUITracker.get("personal_info_lbl_installment_count_result"),
                "total_payment": GUITracker.get("personal_info_lbl_total_payment_result"),
                "starting_date": GUITracker.get("personal_info_lbl_starting_date_result"),
                "ending_date": GUITracker.get("personal_info_lbl_ending_date_result"),
                "loan_count": GUITracker.get("personal_info_lbl_loan_count_result"),
                "work_status": GUITracker.get("personal_info_lbl_work_status_result")
            }
            return info_widget_dic

        @classmethod
        def display_default(cls):
            """user info section"""
            
            for widget in cls.get_info_widget_dic().values():
                widget.config(text=" ")

        @classmethod
        def display_borrower(cls, user_info_dic):
            """a dictionary of widgets corresponding to  a dictionary of user info """

            d = cls.get_info_widget_dic()

            d["loan_recipient"].config(text=user_info_dic["first_name"] + " " + user_info_dic["last_name"])
            d["employee_id"].config(text=user_info_dic["employee_id"])
            d["national_id"].config(text=user_info_dic["national_id"])

            text = Search.GeneralStatusDescription.general_status_value(user_info_dic["general_status"], user_info_dic["registration_date"])
            d["general_status"].config(text=text)

            d["bank"].config(text="saman")
            d["branch"].config(text=user_info_dic["branch_id"])
            d["loan_amount"].config(text=CommonUtil.format_number_comma_separated(user_info_dic["loan_amount"]))
            d["installment_amount"].config(text=CommonUtil.format_number_comma_separated(user_info_dic["installment_amount"]))

            d["account_number"].config(text=user_info_dic["account_num"])
            d["file_number"].config(text=user_info_dic["file_num"])
            d["installment_count"].config(text=user_info_dic["installment_num"])
            d["total_payment"].config(text=CommonUtil.format_number_comma_separated(user_info_dic["total_payment"]))

            d["starting_date"].config(text=user_info_dic["starting_date"])
            d["ending_date"].config(text=user_info_dic["ending_date"])
            d["loan_count"].config(text=user_info_dic["loan_count"])
            d["work_status"].config(text=user_info_dic["work_status_id"])
