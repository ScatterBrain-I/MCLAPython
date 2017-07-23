# Program by Peter Niemeyer 2017/07/23
# MCLA Python / Mark Cohen
# This program:
# Allows a user to input a bird name regardless of capitalization 
# to be checked aginst a .txt file (list form) for tallied sightings of 
# said bird. The max number of sightings is also offered. The user may 'exit'
# any time.
# NOTE: I changed the original Cardinal data to tally '9' instead of '10' 
# to demonstarte that 'max sightings' ties would display multiple birds. 

import NEMO

# Change filename to import any datafile formatted: [name], [# of sightings]
# Names mus be consistent in the file, multiple entries can be used per name
filename = "Birds.txt"


# PROF COHEN INSTRUCTIONS:------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
    d = {}
    for line in open (filename):
        temp = line.split(",")
        bird = temp[0].lower().strip()
        sightings = int(temp[1].strip())
        # Tally Function
        if bird in d:
            sightings = sightings + d[bird]
            d[bird] = sightings
        else:     
            d[bird] = sightings
    return d

# Determines the 'key' in 'd' (defined in countBirds(filename) 
# that has the highest value and writes that key to a list mostSeen[]
def mostSeen(d):
    d = countBirds(filename)
    mostSeen = []
    for k in d.keys():
        most = max([i for i in d.values()])
        if d[k] == most:
            mostSeen.append(k.title())
    return mostSeen
    
# Creates a variable 'most' that is the highest value form countBirds(filename)    
def most():
    d = countBirds(filename)
    most = max([i for i in d.values()])
    return most

# Asks the user to enter a bird name and then looks up the sighting count 
# for that bird in the specified dictionary (d).
def askUser(d):
    d = countBirds(filename)
    inquiry = NEMO.userString("Enter a bird name (Type 'Exit' to finish):").lower()
    if inquiry in d:
        return "The %s has been seen %i times.\n" % (inquiry.title(), d[inquiry])
    elif inquiry == "exit":
        print "Good bye.\n"
        quit()   ## breaks out of the continuous loop started in main()
    else:
        return "The %s has not been seen yet (Check your spelling of '%s'). \n\
Birds in list: %s \n" % (inquiry.title(), inquiry.title(), d.keys())

# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
def main():
    e = 0
    while e == 0: # Creates a continuous loop which can be broken in askUser(d) 
        d = countBirds(filename)
        print askUser(d)
        print "The following bird have been seen the most (%i) times: %s\n" % (most(), mostSeen(d))
    
main()
