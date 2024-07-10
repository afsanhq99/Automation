# utilities/excel_utils.py
import openpyxl

def read_excel(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        data.append((username, password))
    return data

def get_test_data(file_path, sheet_name):
    return read_excel(file_path, sheet_name)