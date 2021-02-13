#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

sauce = requests.get('https://unicode-table.com/en/sets/arrow-symbols/#right-arrows').text
soup = BeautifulSoup(sauce, 'lxml')

a_tag = soup.find_all('a')

for a in a_tag:
    try:
        print(a['data-symbol'], end='  ')
    except KeyError:
        pass
