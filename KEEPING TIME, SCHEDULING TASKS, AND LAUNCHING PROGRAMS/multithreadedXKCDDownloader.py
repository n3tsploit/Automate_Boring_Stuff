import os, requests, bs4
import threading

os.makedirs('xkcd', exist_ok=True)


def xcd(beginning, ending):
    for image in range(beginning, ending):
        res = requests.get(f'https://xkcd.com/{image}')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        image_elements = soup.select('#comic img')
        if not image_elements:
            print('No Image Found')
        else:
            image_url = 'https:' + image_elements[0].get('src')
            print(f'Downloading {image_url}')
            res = requests.get(image_url)
            res.raise_for_status()
            with open('./xkcd/' + os.path.basename(image_url), 'wb') as r:
                r.write(res.content)
            print(f'{os.path.basename(image_url)} Done')


download_threads = []

for i in range(0, 40, 10):
    start = i
    stop = i + 9
    if start == 0:
        start = 1
    download_thread = threading.Thread(target=xcd, args=(start, stop))
    download_threads.append(download_thread)
    download_thread.start()
print(download_threads)

for i in download_threads:
    i.join()
print(download_threads)


"""
In Chapter 12, you wrote a program that downloaded all of the XKCD comic strips from the XKCD
website. This was a single-threaded program: it downloaded one comic at a time. Much of the program’s
running time was spent establishing the network connection to begin the download and writing the
downloaded images to the hard drive. If you have a broadband internet connection, your single-threaded
program wasn’t fully utilizing the available bandwidth.
A multithreaded program that has some threads downloading comics while others are establishing
connections and writing the comic image files to disk uses your internet connection more efficiently and
downloads the collection of comics more quickly. Open a new file editor tab and save it as
threadedDownloadXkcd.py . You will modify this program to add multithreading.
"""