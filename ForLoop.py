import NEMO

word = NEMO.userString("Please enter a word:")

for letter in word:
    letter = letter + " "
    print letter, 

print "\nAll done!"    

words = ['cat', 'dog', 'chicken', 'house', 'barber']
lengths = []
for word in words:
    l = len(word)
    lengths.append(l)
print words    
print "Here are the lengths %s" % lengths    