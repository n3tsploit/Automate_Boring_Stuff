import csv
import os

from path import Path

p = Path('.')

os.makedirs('headerRemoved', exist_ok=True)
for file in list(p.glob('*.csv')):
    rows = []
    with open(f'{file}') as r:
        data = csv.reader(r)
        for row in data :
            if data.line_num == 1:
                continue
            rows.append(row)
        for item in rows:
            with open(f'./headerRemoved/{file}', 'a', newline='') as w:
                content = csv.writer(w)
                content.writerow(item)
    print(rows)

"""
Say you have the boring job of removing the first line from several
hundred CSV files. Maybe you’ll be feeding them into an automated
process that requires just the data and not the headers at the top of the
columns. You could open each file in Excel, delete the first row, and resave
the file—but that would take hours. Let’s write a program to do it
instead.
The program will need to open every file with the .csv extension in the
current working directory, read in the contents of the CSV file, and
rewrite the contents without the first row to a file of the same name. This
will replace the old contents of the CSV file with the new, headless
contents.
"""