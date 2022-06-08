import os
import re
import shutil

date_pattern = re.compile(r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$')

for file_name in os.listdir('.'):
    mo = date_pattern.search(file_name)
    if mo is not None:
        before = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        after = mo.group(8)

        new_name = before + day + '-' + month + '-' + year + after

        file_name = os.path.join(os.path.abspath('.'), file_name)
        new_name = os.path.join(os.path.abspath('.'), new_name)
        print(f'renaming {file_name} to {new_name}\n')
        shutil.move(file_name, new_name)

"""
Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to European-
style dates (DD-MM-YYYY).
"""