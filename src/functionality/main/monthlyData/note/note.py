from src.datatbase.dbQuery import DBQuery
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.messageUtil import MessageUtil
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class Note:

    @classmethod
    @run_func_disp_err_ret_brk
    def save(cls):
        """reads the note and save it"""

        period = MonthlyDataUtil.get_period(output_type="int")
        note = GUIUtil.read_textbox(GUITracker.get("monthly_data_note_txt_note"))
        cls.store(period, note)
        MessageUtil.show_message(1, "Note saved.")
        return "break"

    @staticmethod
    def store(period, text):
        """Stores text in the DB where summary of monthly data is stored"""

        query_string = f"""INSERT INTO Saman_Monthly_Data_Data_Summary (period, note)
                                       VALUES({period}, "{text}")
                                       ON CONFLICT(period) DO UPDATE SET note = "{text}" ;
                                     """
        DBQuery.dml_query(query_string)
