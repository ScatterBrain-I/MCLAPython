import random
import time
import NEMO

number = [0,0,0] 
name = ['Moe', 'Larry', 'Curly']

# function that creates a list of three random dogs eaten with different rates 
# so the game is rigged. 'number' will increase through game, 'dogseat' will 
# reset each time this function runs
def sortOfRandDogs():
    dogsEat = [0,0,0]
    #Moe's rate 1-3
    #Larry's rate 1-4
    #Curly's rate 1-5 (Best bet is here!)
    for i in range (0, 3):
        dogsEat[i] = random.randrange(1, 4+i)
    for i in range (0, 3):
        number[i] += dogsEat[i]
    return number    

# function that prints the status of how many dogs have been eaten
def printDogStatus():
    for i in range (0, 3):
        print "%s has eaten %i hot dogs!" % (name[i], number[i])
        i =+ 1

# function that determines the winner by comparing maxnumber with list of totals
def determineWinner():
    winner = ""
    for i in range (0, 3):
        if number[i] == max(number):
            winner = name[i]
    return winner

# Place a bet on a hot dog eating contest that might just be less than random     
def main():
    # starting cash
    money = 100
    # start of main loop
    go = True
    while go == True:
        pick = ""
        while not pick in name: # only allows proper input
            pick = NEMO.userString("Who do you think will win? (Moe, Larry, or Curly):")
        # collects a bet for the contest
        wager = NEMO.userInt("How much do you want to wager on this contest? \
(You have $%i):" % money)
        # if user enters too much, the bet is adjusted 
        if wager > money:
            print ("You do not have that much money. I will accept a bet of %i" % money)
            wager = money    
        #loops the contest until one of the totals clears 50
        while max(number) < 51:
            print "\nnom... nom... nom...\n"
            time.sleep(1)
            sortOfRandDogs()
            printDogStatus()
        #having looped teh contest a winner muct be determined
        # also amount of the bet is added or subtracted - total offered
        determineWinner()
        winner = determineWinner()
        if winner == pick:
            print "\nYou picked the winner, %s." % winner
            money = (money + wager)
        else:
            print "\nYou did not pick the winner, %s." % winner
            money = (money - wager)       
        print "Your total holdings are $%s\n" % money
        # if you go broke you are kicked out, otherwise you loop
        if money == 0:
            print "You are broke and are done here!"
            go = False
        else:
            # resets the number count
            for i in range (0, 3):
                number[i] = 0
            go = True
main()        


