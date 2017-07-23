import NEMO
d = {}
for line in open('DictionaryGrades.txt'):
    temp = line.split (":")
    name = temp[0].strip()
    grades = temp[1].split(',')
    for index in range(0, len(grades)):
        grades[index] = grades[index].strip()
    d[name] = grades

n = NEMO.userString("Enter a name:")
if n in d:
    print d[n]
else:
    print "%s is not in the file." % n
    
