name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
names = []

for line in handle:
    if line.startswith('From'):
        line = line.split()
        if len(line) > 2:
            names.append(line[1])
            

for name in names:
    counts[name] = counts.get(name, 0) +1


bigcount = None
bigname = None
for name, count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count
        
print (bigname, bigcount)