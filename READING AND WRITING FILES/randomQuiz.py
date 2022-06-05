import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz in range(35):
    states = list(capitals.keys())
    random.shuffle(states)
    with open(f'paper{quiz +1 }.txt', 'w') as paper:
        paper.write('Name:\nClass:\nDate:\n\t\t\t\tAnswer the following questions\n')
        paper.write('_' * 90)
        for question in range(50):
            correct_answer = capitals[states[question]]
            wrong_answer = list(capitals.values())
            wrong_answer.remove(correct_answer)
            wrong_answer = random.sample(wrong_answer, 3)
            answer_options = wrong_answer + [correct_answer]
            random.shuffle(answer_options)

            paper.write(f'\nWhat is the capital city of {states[question]} ?\n')
            for i in range(4):
                paper.write(f'{"ABCD"[i]}. {answer_options[i]}\n')
            with open(f'answersheet{quiz + 1}', 'a') as answer_sheet:
                answer_sheet.write(f'{question + 1}. {"ABCD"[answer_options.index(correct_answer)]}\n')

print('Done!!')

"""
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state
capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to
randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib
answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately,
you know some Python.
"""
