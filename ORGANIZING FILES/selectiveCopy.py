import os
import re
import shutil

name_regex = re.compile(r'(.*)(\.pdf|\.png)')
folder = '/'
count = 0
for folder_name, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        mo = name_regex.search(filename)
        if mo is not None:
            file_location = os.path.join(folder_name, filename)
            file_destination = '/home/netsploit/Desktop/pics'
            try:
                shutil.copy(file_location, file_destination)
                count = count + 1
            except shutil.SameFileError:
                continue

print(f'{count} files copied.')

"""
Write a program that walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg ). Copy these files from
whatever location they are in to a new folder.
"""