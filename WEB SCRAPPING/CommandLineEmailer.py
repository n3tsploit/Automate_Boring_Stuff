# I used tutanota mail server
# First argument is the recipient email adress and the other arguments are the content os the email
import pyinputplus
import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

if len(sys.argv) > 2:
    email_regex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)
    if email_regex.search(sys.argv[1]):
        email_adress = sys.argv[1]
        email_content = ' '.join(sys.argv[2:])

        my_email = pyinputplus.inputEmail('Enter your email address: ')
        my_password = pyinputplus.inputPassword('Enter password: ')

        browser = webdriver.Firefox(executable_path='./geckodriver')

        browser.get('https://mail.tutanota.com/login')

        email_elem = browser.find_elements_by_class_name('input')
        email_elem[0].send_keys(my_email)
        email_elem[1].send_keys(my_password)
        button_elem = browser.find_element_by_tag_name('button')
        button_elem.click()

        WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.LINK_TEXT, "Inbox")))
        new_email = browser.find_elements_by_tag_name("button")
        new_email[-2].click()

        time.sleep(3)
        inputs = browser.find_elements_by_tag_name('input')
        inputs[0].send_keys(email_adress)
        inputs[1].send_keys('no subject')

        content = browser.find_element_by_link_text('--')
        content.send_keys(email_content)

        send_button = browser.find_elements_by_link_text('submit')
        send_button.submit()
    else:
        print('Wrong email format')
else:
    print('Pass email address and text to be sent as the arguments')


"""
Write a program that takes an email address and string of text on the command line and then, using selenium ,
logs in to your email account and sends an email of the string to the provided address. (You might want to
set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs. You could also write a similar
program to send messages from a Facebook or Twitter account.
"""
