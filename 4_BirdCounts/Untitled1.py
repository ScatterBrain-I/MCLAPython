
d = {}
for line in open ("Birds.txt"):
    temp = line.split(",")
    bird = temp[0].strip()
    sightings = int(temp[1].strip())
    if bird in d:
        sightings = sightings + d[bird]
        d[bird] = sightings
    else:     
       d[bird] = sightings

bird = "Robin"

for k in d.keys():
    if d[k] == 4:
        print bird    

