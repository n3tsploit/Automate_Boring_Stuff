import shelve, pyperclip, sys

with shelve.open('mcb') as db:
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        db[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del db[sys.argv[2]]
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            pyperclip.copy(list(db.keys()))
        elif sys.argv[1] == 'delete':
            db.clear()
        elif sys.argv[1] in db:
            pyperclip.copy(db[sys.argv[1]])

db.close()

"""
Extend the multi-clipboard program in this chapter so that it has a delete <keyword> command line argument
that will delete a keyword from the shelf. Then add a delete command line argument that will delete all
keywords.
"""
