from src.functionality.main.monthlyCalculation.response.response import Response
from src.functionality.decorator.decorator import db_open_run_commit
from src.functionality.decorator.decorator import update_db_invalid_data


class ComptrollerRequest(Response):
    data_column_name = "comptroller_req"
    config_column_name = "comptroller_req_sum"
    sum_lbl_name = "monthly_calc_response_lbl_comptroller_req_sum"


class ComptrollerResponse(Response):
    data_column_name = "comptroller_res"
    config_column_name = "comptroller_res_sum"
    sum_lbl_name = "monthly_calc_response_lbl_comptroller_res_sum"


class InsuranceResponse(Response):
    data_column_name = "insurance_res"
    config_column_name = "insurance_res_sum"
    sum_lbl_name = "monthly_calc_response_lbl_insurance_res_sum"


class RetiresResponse(Response):
    data_column_name = "retires_res"
    config_column_name = "retires_res_sum"
    sum_lbl_name = "monthly_calc_response_lbl_retires_res_sum"


class OverdueResponse(Response):
    data_column_name = "overdue_res"
    config_column_name = "overdue_res_sum"
    sum_lbl_name = "monthly_calc_response_lbl_overdue_res_sum"

    class DataStorage(Response.DataStorage):
        @staticmethod
        @update_db_invalid_data
        @db_open_run_commit
        def store(cur, table_name, column_name, data):
            """update DB according to the given data"""

            query_string = f"UPDATE {table_name} SET {column_name} = 0"
            cur.execute(query_string)

            query_string = f"""
                                UPDATE {table_name} SET {column_name} = ? WHERE
                                employee_id = (SELECT employee_id FROM Saman_Info WHERE national_id = ?);
                            """
            cur.executemany(query_string, data)



