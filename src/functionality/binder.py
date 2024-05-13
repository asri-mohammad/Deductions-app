from src.gui.guiTracking.guiTracker import GUITracker as T

import src.functionality.menu.applications.applications

import src.functionality.util.commonCommand.sample
from src.functionality.constants.resourcePath.samplePath import SamplePath

import src.functionality.retires.division.fileSelection
import src.functionality.retires.division.division
import src.functionality.retires.division.fileSaving

import src.functionality.retires.request.fileSelection
import src.functionality.retires.request.request
import src.functionality.retires.request.fileSaving

import functionality.main.monthlyCalculation.setting.restart
import functionality.main.monthlyCalculation.setting.periodSelection

import functionality.main.monthlyCalculation.workStatus.workStatusUpdate
import functionality.main.monthlyCalculation.workStatus.unknownList
import functionality.main.monthlyCalculation.workStatus.workStatusState

import functionality.main.info.generalStatus
import functionality.main.info.search
import functionality.main.info.individualReport

import functionality.main.monthlyCalculation.response.responseSubClasses

import functionality.main.monthlyCalculation.bankList.bankList
import functionality.main.monthlyCalculation.bankList.bankLetter

import functionality.main.monthlyCalculation.request.comptrollerRequest
import functionality.main.monthlyCalculation.request.retiresRequest
import functionality.main.monthlyCalculation.request.insuranceRequest
import functionality.main.insuranceSetting.change.eligibleChange
import functionality.main.insuranceSetting.change.reasonChange
import functionality.main.insuranceSetting.update.reasonUpdate
import functionality.main.insuranceSetting.update.eligibleUpdate

import functionality.main.monthlyData.setting.periodSelection
import functionality.main.monthlyData.setting.restart
import functionality.main.monthlyData.data.dataStorageSubs
import functionality.main.monthlyData.data.BankListDataStorage
import functionality.main.monthlyData.data.overdueDataStorage
import functionality.main.monthlyData.data.monthlyReport
import functionality.main.monthlyData.note.note

import src.functionality.backup.directorySelection
import src.functionality.backup.exportation
import src.functionality.backup.importation

import functionality.main.batchOperation.update.residueUpdate
import functionality.main.batchOperation.update.generalStatusUpdate

import functionality.main.batchOperation.fullReport.fullReport


class Binder:

    @staticmethod
    def bind():
        """a place where all bindings happen"""

        # menu
        #   applications
        src.functionality.menu.applications.applications.Applications.cmd_applications_main_page()
        src.functionality.menu.applications.applications.Applications.cmd_applications_retirement_utils()
        src.functionality.menu.applications.applications.Applications.cmd_applications_backup()

        # retirement division
        T.get("division_btn_openFile").bind("<Button-1>", lambda e:
        src.functionality.retires.division.fileSelection.FileSelection.select())
        T.get("division_btn_calculate").bind("<Button-1>", lambda e:
        src.functionality.retires.division.division.Division.generate())
        T.get("division_btn_save").bind("<Button-1>", lambda e:
        src.functionality.retires.division.division.FileSaving.save())
        T.get("division_btn_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.division.value))

        # retirement request list
        T.get("retirement_request_btn_openFile").bind("<Button-1>", lambda e:
        src.functionality.retires.request.fileSelection.FileSelection.select())
        T.get("retirement_request_btn_calculate").bind("<Button-1>", lambda e:
        src.functionality.retires.request.request.Request.generate())
        T.get("retirement_request_btn_save").bind("<Button-1>", lambda e:
        src.functionality.retires.request.fileSaving.FileSaving.save())
        T.get("retirement_request_btn_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.retirement_req_list.value))

        # info
        #   general status
        T.get("general_status_btn_register").bind("<Button-1>", lambda e:
        functionality.main.info.generalStatus.GeneralSatus.register())

        #   search
        T.get("info_search_btn_search").bind("<Button-1>", lambda e:
        functionality.main.info.search.Search.search())
        T.get("info_search_btn_search").bind("<Return>", lambda e:
        functionality.main.info.search.Search.search())

        #   report
        T.get("personal_info_btn_report").bind("<Button-1>", lambda e:
        functionality.main.info.individualReport.IndividualReport.generate())

        # monthly calculation
        #   setting
        T.get("monthly_calculation_setting_btn_reset").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.setting.restart.Restart.reset())
        T.get("monthly_calculation_setting_cmb_period").bind("<<ComboboxSelected>>", lambda e:
        functionality.main.monthlyCalculation.setting.periodSelection.PeriodSelection.store())

        #   Work status
        T.get("monthly_calculation_btn_work_status_update_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.work_status.value))
        T.get("monthly_calculation_btn_work_status_update").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.workStatus.workStatusUpdate.WorkStatusUpdate.update())
        T.get("monthly_calculation_btn_unknown_list_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.unknown_list.value))
        T.get("monthly_calculation_btn_unknown_list").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.workStatus.unknownList.UnknownList.generate())
        T.get("monthly_calculation_chb_var_is_work_status_updated").trace("w", lambda x, y, z:
        functionality.main.monthlyCalculation.workStatus.workStatusState.WorkStatusState.update())

        #   responses
        T.get("monthly_calc_response_btn_comptroller_req_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_comptroller_request.xlsx"))
        T.get("monthly_calc_response_btn_comptroller_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_comptroller_response.xlsx"))
        T.get("monthly_calc_response_btn_retires_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_retires_response.xlsx"))
        T.get("monthly_calc_response_btn_insurance_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_insurance_response.xlsx"))
        T.get("monthly_calc_response_btn_overdue_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.national_id_money.value, "sample_overdue_response.xlsx"))

        T.get("monthly_calc_response_btn_comptroller_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.response.responseSubClasses.ComptrollerRequest.set())
        T.get("monthly_calc_response_btn_comptroller_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.response.responseSubClasses.ComptrollerResponse.set())
        T.get("monthly_calc_response_btn_retires_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.response.responseSubClasses.RetiresResponse.set())
        T.get("monthly_calc_response_btn_insurance_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.response.responseSubClasses.InsuranceResponse.set())
        T.get("monthly_calc_response_btn_overdue_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.response.responseSubClasses.OverdueResponse().set())

        #   bank list
        T.get("monthly_calc_bank_list_btn_generate").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.bankList.bankList.BankList.generate())
        T.get("monthly_calc_bank_list_btn_letter").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.bankList.bankLetter.BankLetter.generate())
        #   request
        T.get("monthly_calc_request_btn_comptroller_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.request.comptrollerRequest.ComptrollerRequest.generate())
        T.get("monthly_calc_request_btn_retires_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.request.retiresRequest.RetiresRequest.generate())
        T.get("monthly_calc_request_btn_insurance_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyCalculation.request.insuranceRequest.InsuranceRequest.generate())
        T.get("monthly_calc_request_btn_insurance_reasons").bind("<Button-1>", lambda e:
        functionality.main.insuranceSetting.change.reasonChange.ReasonChange.open())
        T.get("monthly_calc_request_btn_insurance_reasons_update").bind("<Button-1>", lambda e:
        functionality.main.insuranceSetting.update.reasonUpdate.ReasonUpdate.update())
        T.get("monthly_calc_request_btn_insurance_eligible").bind("<Button-1>", lambda e:
        functionality.main.insuranceSetting.change.eligibleChange.EligibleChange.open())
        T.get("monthly_calc_request_btn_insurance_eligible_update").bind("<Button-1>", lambda e:
        functionality.main.insuranceSetting.update.eligibleUpdate.EligibleUpdate.update())

        # Monthly Data
        #   setting
        T.get("monthly_data_period_setting_cmb_period").bind("<<ComboboxSelected>>", lambda e:
        functionality.main.monthlyData.setting.periodSelection.PeriodSelection.update())
        T.get("monthly_data_period_setting_btn_reset").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.setting.restart.Restart.reset())

        #   data/setting data
        T.get("monthly_data_data_btn_comptroller_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.ComptrollerResDataStorage.store())
        T.get("monthly_data_data_btn_retires_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.RetiresResDataStorage.store())
        T.get("monthly_data_data_btn_insurance_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.InsuranceResDataStorage.store())

        T.get("monthly_data_data_btn_bank_list").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.BankListDataStorage.BankListDataStorage.store())
        T.get("monthly_data_data_btn_other").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.OtherDataStorage.store())

        T.get("monthly_data_data_btn_overdue_res").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.overdueDataStorage.OverdueDataStorage.store())
        T.get("monthly_data_data_btn_comptroller_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.ComptrollerReqDataStorage.store())
        T.get("monthly_data_data_btn_retires_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.RetiresReqDataStorage.store())
        T.get("monthly_data_data_btn_insurance_req").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.dataStorageSubs.InsuranceReqDataStorage.store())

        #   data/sample
        T.get("monthly_data_data_btn_comptroller_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_comptroller_response.xlsx"))
        T.get("monthly_data_data_btn_retires_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_retires_response.xlsx"))
        T.get("monthly_data_data_btn_insurance_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_insurance_response.xlsx"))

        T.get("monthly_data_data_btn_bank_list_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.national_id_money.value, "sample_bank_list.xlsx"))
        T.get("monthly_data_data_btn_other_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.national_id_money.value, "sample_other_list.xlsx"))

        T.get("monthly_data_data_btn_overdue_res_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.national_id_money.value, "sample_overdue_response.xlsx"))
        T.get("monthly_data_data_btn_comptroller_req_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_comptroller_request.xlsx"))
        T.get("monthly_data_data_btn_retires_req_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_retires_request.xlsx"))
        T.get("monthly_data_data_btn_insurance_req_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.employee_id_money.value, "sample_insurance_request.xlsx"))

        #   data/monthly report
        T.get("monthly_data_data_btn_monthly_report").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.data.monthlyReport.MonthlyReport.generate())

        #   note
        T.get("monthly_data_note_btn_save").bind("<Button-1>", lambda e:
        functionality.main.monthlyData.note.note.Note.save())

        # Backup
        T.get("backup_btn_select_dir").bind("<Button-1>", lambda e:
        src.functionality.backup.directorySelection.DirectorySelection.cmd_select_directory())
        T.get("backup_btn_export").bind("<Button-1>", lambda e:
        src.functionality.backup.exportation.Exportation.cmd_export())
        T.get("backup_btn_import").bind("<Button-1>", lambda e:
        src.functionality.backup.importation.Importation.cmd_import())

        # batch operation
        #   update
        T.get("batch_operation_update_btn_residue").bind("<Button-1>", lambda e:
        functionality.main.batchOperation.update.residueUpdate.ResidueUpdate.cmd_batch_update())
        T.get("batch_operation_update_btn_residue_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.residue_update.value))
        T.get("batch_operation_update_btn_general_status").bind("<Button-1>", lambda e:
        functionality.main.batchOperation.update.generalStatusUpdate.GeneralStatusUpdate.cmd_batch_update())
        T.get("batch_operation_update_btn_general_status_sample").bind("<Button-1>", lambda e:
        src.functionality.util.commonCommand.sample.Sample.cmd_sample(SamplePath.general_statu_update.value))

        #   full report
        T.get("batch_operation_full_report_btn_full_report").bind("<Button-1>", lambda e:
        functionality.main.batchOperation.fullReport.fullReport.FullReport.generate_report())







