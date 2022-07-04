import json
import os
import requests
from dotenv import load_dotenv
import sys

load_dotenv()


if len(sys.argv) < 2:
    print('USE: python3 FetchingCurrentWeatherData.py cityname, country abbreviation i.e KE for kenya')
else:
    location = ''.join(sys.argv[1:]).strip()
    api_key = os.environ.get('weather_key')
    url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={api_key}'
    content = requests.get(url)
    content.raise_for_status()
    print(content.text)
    data = json.loads(content.text)  # Api key is not working...recheck later

"""
Checking the weather seems fairly trivial: Open your web browser, click
the address bar, type the URL to a weather website (or search for one and
then click the link), wait for the page to load, look past all the ads, and so
on.
Actually, there are a lot of boring steps you could skip if you had a
program that downloaded the weather forecast for the next few days and
printed it as plaintext. This program uses the requests module from
Chapter 12 to download data from the web.
"""
