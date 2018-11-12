import openpyxl

wb = openpyxl.load_workbook("Book1.xlsx")
sheetname = 'Sheet1'
data = wb.get_sheet_by_name(sheetname)
rows = data.rows
for row in rows:
    if row[0].value == 11:
        row[1].value = "Priya"
        print(row[0].value, row[1].value)
wb.save("Book1.xlsx")