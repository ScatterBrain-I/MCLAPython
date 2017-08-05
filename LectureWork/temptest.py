name = []
name.append("bad boy")
name.append("bad boys")

name[0] = "wordish"

print name



for f in files:
        for line in open(f):
            line2 = line.upper()
            if search in line2:
                counter = counter + 1
                print "%s: %s" %(f, line)
