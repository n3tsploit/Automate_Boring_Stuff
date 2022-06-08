import os

folder = '/'

for folder_name, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        file_path = os.path.join(folder_name, filename)
        try:
            file_size = os.path.getsize(file_path)
            if file_size > 100000000:
                print(f'{file_path} is gretater than  100MB, it\'s size is {file_size} bytes.')
                # code to delete the files can be entered here <:)
                # os.unlink(file_path)
        except FileNotFoundError:
            continue
        except PermissionError:
            continue

print('Done')

"""
It’s not uncommon for a few unneeded but humongous files or folders to
take up the bulk of the space on your hard drive. If you’re trying to free
up room on your computer, you’ll get the most bang for your buck by
deleting the most massive of the unwanted files. But first you have to find
them.
Write a program that walks through a folder tree and searches for
exceptionally large files or folders—say, ones that have a file size of more
than 100MB. (Remember that to get a file’s size, you can use
os.path.getsize() from the os module.) Print these files with their absolute
path to the screen.

"""
