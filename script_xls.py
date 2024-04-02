# for xls pip install xlrd
from xlrd import open_workbook

workbook = open_workbook("tmp/example2.xls")
print(workbook.nsheets)  # количество листов
print(workbook.sheet_names())
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(rowx=1, colx=1))

for rx in range(sheet.nrows):
    print(sheet.row(rx))
