from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.util.guiUtil import GUIUtil
from src.functionality.util.commonUtil import CommonUtil


class DataDisplay:

    @staticmethod
    def get_widgets():
        """creating a list of widgets in their of their appearance"""

        widget_list = [
            GUITracker.get("monthly_data_data_lbl_comptroller_res"),
            GUITracker.get("monthly_data_data_lbl_retires_res"),
            GUITracker.get("monthly_data_data_lbl_insurance_res"),
            GUITracker.get("monthly_data_data_lbl_res_sum"),
            GUITracker.get("monthly_data_data_lbl_bank_list"),
            GUITracker.get("monthly_data_data_lbl_other"),
            GUITracker.get("monthly_data_data_lbl_bank_sum"),
            GUITracker.get("monthly_data_data_lbl_overdue_res"),
            GUITracker.get("monthly_data_data_lbl_comptroller_req"),
            GUITracker.get("monthly_data_data_lbl_retires_req"),
            GUITracker.get("monthly_data_data_lbl_insurance_req"),
            GUITracker.get("monthly_data_data_lbl_req_sum"),
            GUITracker.get("monthly_data_note_txt_note")
                    ]

        return widget_list

    @classmethod
    def set_all_to_default(cls):
        """setting all the widgets to the default value"""

        widget_list = cls.get_widgets()

        # setting first 12 widgets to zero
        for i in range(0, 12):
            GUIUtil.clear_write_label_widget(widget_list[i], "0")
        # setting note textbox
        GUIUtil.clear_write_text_widget(widget_list[12], "")

    @classmethod
    def set_all(cls, values_list):
        """setting all the widgets to the corresponding value in the value_list, values order here matter"""
        widget_list = cls.get_widgets()

        # setting first 12 widgets to zero
        for i in range(0, 12):
            value = 0 if values_list[i] is None else values_list[i]
            value = CommonUtil.format_number_comma_separated(value)
            GUIUtil.clear_write_label_widget(widget_list[i], value)
        # setting note textbox
        value = " " if values_list[12] is None else str(values_list[12])
        GUIUtil.clear_write_text_widget(widget_list[12], value)



