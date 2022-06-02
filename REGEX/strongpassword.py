import re
import pyperclip

password_length = re.compile(r'\w{8,}')
password_uppercse = re.compile(r'[A-Z]+')
password_lowercase = re.compile(r'[a-z]+')
password_digit = re.compile(r'[0-9]+')


def PasswordChecker(password):
    if password_lowercase.search(password) is not None and password_digit.search(
            password) is not None and password_uppercse.search(password) is not None and password_length.search(
            password) is not None:
        print('Password is Strong!!')
    else:
        print('Password is Weak!!')


text = str(pyperclip.paste())
PasswordChecker(text)

"""
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against multiple regex patterns to
validate its strength
"""
