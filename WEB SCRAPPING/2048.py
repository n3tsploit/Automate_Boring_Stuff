import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get('https://gabrielecirulli.github.io/2048/')

center = browser.find_element_by_tag_name('body')

moves = 0
while True:
    time.sleep(0.2)
    choice = random.randint(0, 3)
    if choice == 0:
        center.send_keys(Keys.UP)
    elif choice == 1:
        center.send_keys(Keys.RIGHT)
    elif choice == 2:
        center.send_keys(Keys.DOWN)
    elif choice == 3:
        center.send_keys(Keys.LEFT)
    continue

"""
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys.
You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and
over again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending
up, right, down, and left keystrokes to automatically play the game.

"""
