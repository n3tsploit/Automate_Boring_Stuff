import re

word = str(input('Enter the string: '))
character = str(input('Enter the character you want to strip: '))

if character is not None:
    character = character
else:
    character = ' '

start_strip_regex = re.compile(rf'^{character}')
end_strip_regex = re.compile(rf'{character}$')
result = start_strip_regex.sub(r'', word)
result = end_strip_regex.sub(r'', result)

print(result)

"""
Write a function that takes a string and does the same thing as the strip() string method. If no other
arguments are passed other than the string to strip, then whitespace characters will be removed from the
beginning and end of the string. Otherwise, the characters specified in the second argument to the function
will be removed from the string.
"""
