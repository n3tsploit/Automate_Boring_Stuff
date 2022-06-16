import bs4
import os

import requests

url = 'https://xkcd.com'
os.makedirs('./xkcd', exist_ok=True)
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image_elements = soup.select('#comic img')
    if not image_elements:
        print('could not find image')
    else:
        image_url = 'https:' + image_elements[0].get('src')
        print(f'Downloading {image_url}')
        res = requests.get(image_url)
        res.raise_for_status()
        print(os.path.basename(image_url))
        with open('./xkcd/' + os.path.basename(image_url), 'wb') as r:
            r.write(res.content)

        prev_link = soup.select('a[rel="prev"]')[0].get('href')
        url = 'https://xkcd.com' + prev_link
        print(url)

print("Done!!!!")

"""
Blogs and other regularly updating websites usually have a front page with the most recent post as well as a
Previous button on the page that takes you to the previous post. Then that post will also have a Previous
button, and so on, creating a trail from the most recent page to the first post on the site. If you wanted a
copy of the site’s content to read when you’re not online, you could manually navigate over every page and
save each one. But this is pretty boring work, so let’s write a program to do it instead.
XKCD is a popular geek webcomic with a website that fits this structure (see Figure 12-6). The front page
at https://xkcd.com/ has a Prev button that guides the user back through prior comics. Downloading each
comic by hand would take forever, but you can write a script to do this in a couple of minutes.
"""
