import subprocess
import time

print('Press Enter to start the counter')

for i in range(60, 0, -1):
    time.sleep(1)
    print(f'{(60 - i) + 1} second has elapsed')
    if i == 1:
        subprocess.Popen(['see', 'alarm.wav'])

print('Time Ended')


"""
Just like it’s hard to find a simple stopwatch application, it can be hard to find a simple countdown
application. Let’s write a countdown program that plays an alarm at the end of the countdown.
At a high level, here’s what your program will do:
1. Count down from 60.
2. Play a sound file ( alarm.wav ) when the countdown reaches zero.
This means your code will need to do the following:
1. Pause for 1 second in between displaying each number in the countdown by calling time.sleep() .
2. Call subprocess.Popen() to open the sound file with the default application.
"""