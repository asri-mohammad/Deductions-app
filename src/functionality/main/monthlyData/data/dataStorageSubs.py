from src.functionality.main.monthlyData.data.dataStorage import DataStorage


class ComptrollerResDataStorage(DataStorage):

    column_name_data = "comptroller_res"  # the column where data is stored in it
    column_name_data_sum = "comptroller_res_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "response_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_comptroller_res"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_res_sum"  # name of the widget to display total sum
    flag_data_type = "employee_id"  # it is either employee_id or national_id


class RetiresResDataStorage(DataStorage):

    column_name_data = "retires_res"  # the column where data is stored in it
    column_name_data_sum = "retires_res_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "response_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_retires_res"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_res_sum"  # name of the widget to display total sum
    flag_data_type = "employee_id"  # it is either employee_id or national_id


class InsuranceResDataStorage(DataStorage):

    column_name_data = "insurance_res"  # the column where data is stored in it
    column_name_data_sum = "insurance_res_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "response_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_insurance_res"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_res_sum"  # name of the widget to display total sum
    flag_data_type = "employee_id"  # it is either employee_id or national_id


class OtherDataStorage(DataStorage):

    column_name_data = "other"  # the column where data is stored in it
    column_name_data_sum = "other_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "bank_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_other"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_bank_sum"  # name of the widget to display total sum
    flag_data_type = "national_id"  # it is either employee_id or national_id


class ComptrollerReqDataStorage(DataStorage):

    column_name_data = "comptroller_req"  # the column where data is stored in it
    column_name_data_sum = "comptroller_req_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "request_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_comptroller_req"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_req_sum"  # name of the widget to display total sum
    flag_data_type = "employee_id"  # it is either employee_id or national_id


class RetiresReqDataStorage(DataStorage):

    column_name_data = "retires_req"  # the column where data is stored in it
    column_name_data_sum = "retires_req_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "request_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_retires_req"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_req_sum"  # name of the widget to display total sum
    flag_data_type = "employee_id"  # it is either employee_id or national_id


class InsuranceReqDataStorage(DataStorage):
    column_name_data = "insurance_req"  # the column where data is stored in it
    column_name_data_sum = "insurance_req_sum"  # the column where the sum of corresponding data is stored in it
    column_name_total_sum = "request_sum"  # the column where the total sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_insurance_req"  # name of the widget to display data sum
    total_sum_widget_name = "monthly_data_data_lbl_req_sum"  # name of the widget to display total sum
    flag_data_type = "employee_id"  # it is either employee_id or national_id

