import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter location: ')
url = urllib.request.urlopen(address)
data = url.read()
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

    
tree = ET.fromstring(data)
counts = tree.findall('.//count')

sums = 0
for n in counts:
    n = int(n.text)
    sums += n

print('Count:', len(counts))
print('Sum:', sums)