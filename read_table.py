import openpyxl


def read_table(path):
    wb = None
    try:
        wb = openpyxl.load_workbook(path, data_only=True)
    except:
        wb = None
    return wb


