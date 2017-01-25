import urllib
import xml.etree.ElementTree as ET


while True:
    url = input('Enter location: ')
    if len(url) < 1 : break

    #url =  urllib.urlencode({'sensor':'false', 'address': address})
    print ('Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    print (data)
    tree = ET.fromstring(data)


    results = tree.findall('.//count') #you can use an XPath selector string to look through the
    # entire tree of XML for any tag named 'count' with the following line of code:
    sum=0
    for count in results:
        sum += int(count.text)
    print(sum)

