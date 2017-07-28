# Program by Peter Niemeyer 2017/07/23
# MCLA Python / Mark Cohen
# Card Shuffler with leveled up option

# This program: 
# builds a list with a full deck of cards
# allows a user to choose a number of shuffles 
# allows user to pick betwen perfect and random shuffling
# deals the top five cards from that shuffled deck

import NEMO
import random

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

    
# asks user for how many times to perfectly shuffle the deck
def userShuffles():
    number = 0
    number = NEMO.userInt("How many shuffles would you like?")
    return number
    
# allows user to pick a perfect shuffle or a rondom one
def userShufType():
    kind = ''
    x = True
    while x == True:
        choice = ['p', 'r']
        kind = NEMO.userString("Would you like a perfect(p) shuffle or random(r)?")
        if kind.lower() in choice:
            x = False
        else:
            print "Try again:"
            x = True
    return kind
    
# builds a full ordered deck of cards from the two lists, 'rank' and 'suit'  
def buildDeck(rank, suit):
    deck = ["%s of %s" % (c, s) for s in suit for c in rank]
    return deck
    
# using 'number' for shuffles, loops that either 'perfectly' or 'randomly'
def shuffle(deck, number, kind):
    for i in range(0,number):
        if kind.lower() == "p":    
            temp1 = [c for c in deck if deck.index(c)%2==0]  
            temp2 = [c for c in deck if deck.index(c)%2==1]
            deck = temp1 + temp2
        else:
            random.shuffle(deck)
    return deck

# picks 1st 5 items from any list this def is called on
def deal(x):
    fiveCard = x[0:5]
    return fiveCard
    
# This is the main program that does the thing it is supposed to do.
def main():
    go = True
    while go == True: # allows loop of program
        deck = buildDeck(rank, suit) # Build's deck
        number = userShuffles() # gets # of shuffles
        kind = userShufType() # gets shuffle type: perfect or random
        shufDeck = shuffle(deck, number, kind) # creates a new output deck
        fiveCard = deal(shufDeck) # slices five cards from top of deck
            #--------------------
            # funny coding easter egg would allow me to deal from bottom of deck
            # this would make the anticipated deals wrong for grading purposes
            # so i didn't do it - but the thought occured to me as whimsical
            #--------------------
        print "\n%s\n" % fiveCard # prints shuffled hand
        go = NEMO.goAgain("Another hand ('y' or 'n')?") # repeats program

main()