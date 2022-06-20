import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
files = ['test.txt', 'me.txt', 'me2.txt']

for file in files:
    row = 0
    column = files.index(file) + 1
    print(file, column)
    with open(f'{file}', 'r') as r:
        lines = r.readlines()
        for line in lines:
            row += 1
            sheet.cell(row=row, column=column).value = line
            print(row,column)
            print(line)

wb.save('ls.xlsx')

"""
Write a program to read in the contents of several text files (you can make the text files yourself) and insert 
those contents into a spreadsheet, with one line of text per row. The lines of the first text file will be in the 
cells of column A, the lines of the second text file will be in the cells of column B, and so on.Use the readlines() 
File object method to return a list of strings, one string per line in the file. For the first file, output the first 
line to column 1, row 1. The second line should be written to column 1, row 2, and so on. The next file that is read 
with readlines() will be written to column 2, the next file to column 3, and so on. 
"""

