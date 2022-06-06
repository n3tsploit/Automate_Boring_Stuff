
new_sentence = []
with open('words.txt','r') as r:
    sentence = r.read().split()
    for i in sentence:
        if 'ADJECTIVE' in i:
            i = input('Enter an adjective: \n')
        elif 'NOUN' in i:
            i = input('Enter a noun: \n')
        elif  'VERB' in i:
            i = input('Enter a verb: \n')

        new_sentence.append(i)

    print(' '.join(new_sentence))
    with open('output.txt', 'w') as output:
        output.write(' '.join(new_sentence))


"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
ADJECTIVE , NOUN , ADVERB , or VERB appears in the text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
"""
