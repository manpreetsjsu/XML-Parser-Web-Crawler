#web crawler / web scrapper

import urllib
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
print(html)
#parsing HTML Data
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
#print(soup)
tags = soup('a')
for tag in tags:    # priting/getting all tags with <a href='......' >
    print('TAG:', tag)
    print ('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)