import NEMO

sentence = NEMO.userString("Please enter a sentence")
words = sentence.split(' ')
print words
largeWords = []
mediumWords = []
smallWords = []

for word in words:
    if len(word) > 5:
        largeWords.append(word)
    elif len(word) > 3:
        mediumWords.append(word)
    else:
        smallWords.append(word)
        
print "Large words:", largeWords      
print "Medium words:", mediumWords
print "Small words:", smallWords