import pythoncom
import win32com.client
from pywintypes import com_error
import os

class Convert:
    def __init__(self, file_name):
        self.file_path = f"{os.getcwd()}/assets/output_excel/" + file_name + ".xlsx"
        self.output_path = f"{os.getcwd()}/assets/output_pdf/" + file_name + ".pdf"
        print(self.file_path)

    def convert_pdf(self):
        # Initialize COM library
        pythoncom.CoInitialize()
        try:
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False
            try:
                print('Start conversion to PDF')
                # Open the workbook
                wb = excel.Workbooks.Open(self.file_path)
                # Export as PDF
                wb.ExportAsFixedFormat(0, self.output_path)
                wb.Close()
                print('Succeeded.')
                return True, self.output_path
            except com_error as e:
                print(f"COM Error: {e}")
                return False, str(e)
            finally:
                excel.Quit()
        finally:
            # Uninitialize COM library
            pythoncom.CoUninitialize()
