# urllib works at application (i.e top) layer of TCP

#make more efficient browser in python than with sockets
#program to read web pages

import urllib
import urllib.request
website =urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')


for data in website:
    print(data.strip())

# WEB SCRAWLING, parsing HTML