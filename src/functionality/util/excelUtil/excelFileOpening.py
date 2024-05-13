import os


class ExcelFileOpening:

    @staticmethod
    def open(file_path):
        """command to open given Excel file in Windows OS"""

        os.system(f'start EXCEL.EXE "{file_path}"')
