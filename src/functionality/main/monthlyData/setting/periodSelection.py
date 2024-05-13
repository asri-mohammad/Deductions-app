from src.datatbase.dbQuery import DBQuery
from src.functionality.main.monthlyData.setting.dataDisplay import DataDisplay
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class PeriodSelection:

    @classmethod
    @run_func_disp_err_ret_brk
    def update(cls):
        """updates all the aspects that need to be updated when a new period is selected"""

        period = MonthlyDataUtil.get_period(output_type="int")
        cls.StorePeriod.store(period)
        data_summary = cls.DataRetrieval.retrieve(period)
        cls.DisplayData.display(data_summary)

    class StorePeriod:

        @staticmethod
        def store(period):
            """given a period as in integer stores it in DB"""

            query_string = f"""
                                UPDATE Saman_Monthly_Data_Config SET period = {period}
                                WHERE row_id = 1;
                            """
            DBQuery.dml_query(query_string)

    class DataRetrieval:
        @staticmethod
        def retrieve(period):
            """returns either None, if there is no such period in DB Or  a tuple like (comptroller_res_sum, ...)"""

            query_string = f"""
                                                SELECT 
                                                comptroller_res_sum ,
                                                retires_res_sum     ,
                                                insurance_res_sum   ,
                                                response_sum        ,
                                                bank_list_sum       ,
                                                other_sum           ,
                                                bank_sum            ,
                                                overdue_sum         ,
                                                comptroller_req_sum ,
                                                retires_req_sum     ,
                                                insurance_req_sum   ,
                                                request_sum         ,
                                                note                
                                                FROM Saman_Monthly_Data_Data_Summary WHERE period = {period};
                                                """

            result = DBQuery.dql_query(query_string)

            return result

    class DisplayData:

        @classmethod
        def display(cls, period_data):
            """if there is no value it sets all to default otherwise to the given values"""

            if not period_data:  # empty, now record for the row
                DataDisplay.set_all_to_default()
            else:
                DataDisplay.set_all(period_data[0])


