import openpyxl

wb = openpyxl.load_workbook('new.xlsx')
sheet = wb['Sheet']

for i in range(2, sheet.max_row + 1):
    produce = 'A' + str(i)
    cost = 'B' + str(i)

    if sheet[produce].value.lower() == 'celery':
        print(sheet[produce].value, sheet[cost].value)
        sheet[cost].value = 1.19
    elif sheet[produce].value.lower() == 'garlic':
        print(sheet[produce].value, sheet[cost].value)
        sheet[cost].value = 3.07
    elif sheet[produce].value.lower() == 'lemon':
        print(sheet[produce].value, sheet[cost].value)
        sheet[cost].value = 1.27

wb.save('new.xlsx')
