import xlrd

workbook = xlrd.open_workbook('1.xls')

sheet = workbook.sheet_by_index(0)

rows = sheet.nrows

cols = sheet.ncols

print(rows, cols)

for r in range(rows):
    for c in range(cols):
        print(sheet.cell_value(r, c))
