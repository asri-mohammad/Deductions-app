from tkinter import simpledialog

from src.gui.guiTracking.guiTracker import GUITracker
from src.datatbase.dbQuery import DBQuery
from src.functionality.main.info.selectedBorrower import SelectedBorrower
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.util.dateUtil import DateUtil


class GeneralSatus:

    @classmethod
    @run_func_disp_err_ret_brk
    def register(cls):
        """change the general status of the selected user to the new status """

        radio_button_variable = GUITracker.get("general_status_rbt_var")
        selected_user_employee_id = SelectedBorrower.get()

        if selected_user_employee_id is None:
            MessageUtil.show_message(2, "Please first select a user.")
            return "break"

        date = cls.DateConfirmation.confirm()
        if date is None:  # cancel button
            return "break"

        new_status = radio_button_variable.get()
        cls.DatatStorage.store(selected_user_employee_id, new_status, date)
        MessageUtil.show_message(1,  "User status changed successfully.")
        return "break"

    class DatatStorage:
        @staticmethod
        def store(user_employee_id, new_status, date):
            """set the user's general status to new_satus in DB for the given date"""

            query_string = f"""
                                UPDATE Saman_General_Status
                                SET general_status = "{new_status}" , registration_date = "{date}"
                                WHERE employee_id = {user_employee_id};
                                """
            DBQuery.dml_query(query_string)

    class DateConfirmation:

        @staticmethod
        def confirm():
            """return a string representing date and None if cancel button is clicked on"""

            current_system_date = DateUtil.today()
            title = "Data confirmation"
            prompt = "Please enter the date:"
            confirmed_date = simpledialog.askstring(title=title, prompt=prompt, initialvalue=current_system_date)
            return confirmed_date


