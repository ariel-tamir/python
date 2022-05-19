import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://www.example.com').read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('p')
for tag in tags:
    print(tag.text)