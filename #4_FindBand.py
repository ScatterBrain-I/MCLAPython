import NEMO

searchBand = NEMO.userString("Enter the band you want to follow:")
file = open('/home/ubuntu/workspace/Python-YouTryIt-Public/concerts.txt', 'r')
for line in file:
    bands = line.split(':')
    for band in bands:
        if band == searchBand:
            print line
print "Have fun and protect your ears."            

print

# Professor's code is much nicer.
file = open('/home/ubuntu/workspace/Python-YouTryIt-Public/concerts.txt', 'r')
for line in file:
    if searchBand in line:
        print line,
print "Have fun and protect your ears."