import requests, os
from selenium import webdriver

url = ' '
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get(url)

link_tags = browser.find_elements_by_tag_name('a')

links = []
for i in link_tags:
    if i.get_attribute('href') is not None and 'http' in i.get_attribute('href'):
        links.append(str(i.get_attribute('href')))
        print(i.get_attribute('href'))

links = set(links)

invalid_links = []
valid_links = []
os.makedirs('./pages', exist_ok=True)
for link in links:
    print(f'Checking {link} ...')
    res = requests.get(link)
    try:
        res.raise_for_status()
    except Exception as exc:
        print(f'There was a problem: {exc}')
    if res.status_code == 404:
        invalid_links.append(link)
        print(f'Broken Link --> {link}')
    else:
        valid_links.append(link)
        with open('./pages/' + os.path.basename(link) + '.html', 'wb') as r:
            r.write(res.content)

print('Done!')

"""
Write a program that, given the URL of a web page, will attempt to download every linked page on the
page. The program should flag any pages that have a 404 “Not Found” status code and print them out as
broken links.
"""
