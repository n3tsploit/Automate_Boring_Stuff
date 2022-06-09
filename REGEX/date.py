import pyperclip
import re

date_regex = re.compile(r'(([0-2]\d|[3][0-1])/([0][1-9]|[1][0-2])/([1-2]\d\d\d))')
text = str(pyperclip.paste())
found = []
for date_found in date_regex.findall(text):
    found.append(date_found[0])

print(found)

"""
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range
from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day
or month   is a single digit, it’ll have a leading zero.
"""
