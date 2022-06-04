import random

import pyinputplus
import time

for i in range(10):
    first = random.randint(0, 9)
    second = random.randint(0, 9)
    answer = first * second
    prompt = f'{first} x {second} = '
    try:
        response = pyinputplus.inputInt(prompt, allowRegexes=[f'^{answer}$'], blockRegexes=[('.*', 'Incorrect!')],
                                        timeout=8, limit=3)
        print('correct!')
        time.sleep(1)

    except pyinputplus.TimeoutException:
        print('Time out!')
        time.sleep(1)
    except pyinputplus.RetryLimitException:
        print('You have Exhausted your tries!')
        time.sleep(1)

"""
To see how much PyInputPlus is doing for you, try re-creating the
multiplication quiz project on your own without importing it. This
program will prompt the user with 10 multiplication questions, ranging
from 0 × 0 to 9 × 9. You’ll need to implement the following features:
If the user enters the correct answer, the program displays
“Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the
program moves on to the next question.
Eight seconds after first displaying the question, the question is
marked as incorrect even if the user enters the correct answer after
the 8-second limit.
"""
