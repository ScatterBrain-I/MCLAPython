# Program by Peter Niemeyer 2017/07/14
# MCLA Python / Mark Cohen

# This program:
# Gets inputs from user: 4 verses, a chorus, a repeat factor
# Assembles inputs into list: V.1, Cx, V.2, Cx, V.3, Cx, V.4, Cx+1 all x2
# LEVEL-UP:
# Verses are CAPITALIZED
# Choruses are lowercased
# A forbidden word 'cookies' is blocked out


import NEMO # Mod file: 'userString', 'userInt' used

# Gets input from user: 4 verseres --> assigns them to list 'versesNew'
# Converts to Uppercase
verses = ['first', 'second', 'third', 'fourth']
versesNew = []
for verse in verses:
    verse = NEMO.userString ("Enter the %s verse:" % verse)
    versesNew.append (verse.upper()) 

# Gets input from user: chorus and repeat factor ---> converts to lowercase
chorus = NEMO.userString ("Enter the chorus:")
chorus = chorus.lower()
repeat = NEMO.userInt ("Enter the chorus repeat:")

# Using list 'song', the verses from 'versesNew' are woven with the choruses
song = []
for verse in versesNew:
    song.append (verse)
    song.append ((chorus + " ") * repeat)
    
# Chorus #4 (located in index 7 is to be +1 of the repeat factor 
# song is to repeat (x2) but the extra "one more time" needs to be deleted 
# prints the song in it's list form
song[7] = ((chorus + " ") * (repeat+1)) 
song.append('...one more time!...')
song = song * 2
del song[17]
print song
print

# prints song formatted properly while removing all occurances of the forbidden 
# word regardless of location in verse or chorus
for versesChorus in song:
    print versesChorus.replace('COOKIES', '_______').replace('cookies',
    '_______')