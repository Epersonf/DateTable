from openpyxl import Workbook


def generate_table(path, matrix):
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active

    # Rows can also be appended
    for vec in matrix:
        ws.append(vec)

    # Save the file
    wb.save(path)
