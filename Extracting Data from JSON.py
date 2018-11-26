import json
import urllib.request, urllib.parse, urllib.error


address = input('Enter location: ')
url = urllib.request.urlopen(address)
data = url.read()
info = json.loads(data)


print ('Retrieving', url)
print ('Retrieved', len(data), 'characters')

counts = info['comments']

sums = 0
for item in counts:
    sums += item['count']

print ('Count:', len(counts))
print ('Sum:', sums)


