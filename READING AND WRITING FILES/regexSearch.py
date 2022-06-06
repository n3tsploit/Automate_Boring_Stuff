import re
from path import Path

folder_path = input('Enter the folder Path: \n')
user_input = input('Enter your Regular Expression: \n')
user_regex = re.compile(rf'{user_input}')

for filename in Path(f'{folder_path}').glob('*.txt'):
    with open(f'{filename}') as r:
        for line in r.readlines():
            mo = user_regex.search(line)
            if mo is not None:
                print(line)

print('Done!!')

"""
Write a program that opens all . txt files in a folder and searches for any line that matches a user-supplied
regular expression. The results should be printed to the screen.
"""