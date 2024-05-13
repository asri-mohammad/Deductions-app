from src.functionality.main.insuranceSetting.change.change import Change
from src.functionality.constants.resourcePath.insuranceUpdatePath import InsuranceUpdatePath


class EligibleChange(Change):

    excel_file_path = InsuranceUpdatePath.eligibles.value
