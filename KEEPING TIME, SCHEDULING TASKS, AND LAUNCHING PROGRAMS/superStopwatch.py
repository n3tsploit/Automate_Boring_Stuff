from time import time

print('Press enter to start the laps and CTRL + C to stop ')
start_time = time()
lap = 1
last_time = start_time

try:
    while True:
        input()
        lap_time = round(time() - last_time, 2)
        total_time = round(time() - start_time)
        print(f'Lap #{lap}: {lap_time} seconds')
        print(f'Total time:{total_time} seconds')
        last_time = time()
        lap += 1
except KeyboardInterrupt:
    print('Done!')


"""
Say you want to track how much time you spend on boring tasks you haven’t automated yet. You don’t
have a physical stopwatch, and it’s surprisingly difficult to find a free stopwatch app for your laptop or
smartphone that isn’t covered in ads and doesn’t send a copy of your browser history to marketers. (It
says it can do this in the license agreement you agreed to. You did read the license agreement, didn’t
you?) You can write a simple stopwatch program yourself in Python.
At a high level, here’s what your program will do:
1. Track the amount of time elapsed between presses of the
new “lap” on the timer.
2. Print the lap number, total time, and lap time.
ENTER
key, with each key press starting a
This means your code will need to do the following:

"""