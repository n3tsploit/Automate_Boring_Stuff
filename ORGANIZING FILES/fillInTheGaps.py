import re
import os
import shutil

i = 1

# regex of the prefix
name_regex = re.compile(r'(spam)(\d+)(\.txt)')
length = 0

# count how many files in the folder match the regex
for filename in os.listdir('.'):
    mo = name_regex.search(filename)
    if mo is not None:
        length += 1

for i in range(length):
    file_name = 'spam' + f'{i:03}' + '.txt'
    file_name = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(file_name):
        print(file_name)
        number = len(os.listdir('.'))
        while number > 0:
            old_name = 'spam' + f'{number:03}' + '.txt'
            old_name = os.path.join(os.getcwd(), old_name)
            if os.path.exists(old_name):
                print(f'Renaming {old_name} to {file_name}')
                shutil.copy2(old_name, file_name)
                break
            else:
                number -= 1

print('Done')

"""
Write a program that finds all files with a given prefix, such as
spam001.txt , spam002.txt , and so on, in a single folder and locates any gaps
in the numbering (such as if there is a spam001.txt and spam003.txt but no
spam002.txt ). Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps into
numbered files so that a new file can be added.
"""