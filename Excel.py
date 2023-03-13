from openpyexcel import Workbook

wb = Workbook()
sheet = wb.active

data = (
    ("Name", "CA1", "CA2", "CA3"),
    ("Rahul", 22, 30, 23),
    ("Vikas", 12, 23, 29),
    ("Vikas", 12, 23, 28),
    ("Vikas", 12, 23, 20),
    ("Vikas", 12, 23, 19),
    ("Vikas", 12, 23, 14)

)

for row in data:
    sheet.append(row)
cell = sheet.cell(row=8, column=4)
cell.value = "=SUM(D2:D7)"
cell.font = cell.font.copy(bold=True)
wb.save("student.xlsx")
