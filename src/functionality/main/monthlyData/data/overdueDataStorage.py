from src.functionality.main.monthlyData.data.dataStorage import DataStorage
from src.gui.guiTracking.guiTracker import GUITracker
from src.functionality.decorator.decorator import run_func_disp_err_ret_brk
from src.functionality.util.excelUtil.excelDataReading import ExcelDataReading
from src.functionality.main.monthlyData.monthlyDataUtil import MonthlyDataUtil


class OverdueDataStorage(DataStorage):

    # no total sum for overdue

    column_name_data = "overdue_res"  # the column where data is stored in it
    column_name_data_sum = "overdue_sum"  # the column where the sum of corresponding data is stored in it
    data_sum_widget_name = "monthly_data_data_lbl_overdue_res"  # name of the widget to display data sum
    flag_data_type = "national_id"  # it is either employee_id or national_id

    @classmethod
    @run_func_disp_err_ret_brk
    def store(cls):

        period = MonthlyDataUtil.get_period(output_type="int")

        reordered_data = ExcelDataReading.choose_read_reorder(2, [1, 0])

        if reordered_data is None:  # cancel button
            return "break"
        else:

            data_is_valid = cls.Storage.store(period, reordered_data, cls.flag_data_type, cls.column_name_data)

            if not data_is_valid:
                return "break"

            cls.DataSumStorage.store_column_sum(period, cls.column_name_data, cls.column_name_data_sum)

            data_sum_widget = GUITracker.get(cls.data_sum_widget_name)
            cls.SumDisplay.update_displayed_sum(period, cls.column_name_data_sum, data_sum_widget)

            return "break"