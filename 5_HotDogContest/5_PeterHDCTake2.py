# Program by Peter Niemeyer 2017/07/23
# Version 2.0
# MCLA Python / Mark Cohen

# This program: simulates an unfair hot dog eating contest after taking wagers 
# from the user. 
# This is take two based upon the conversation we had this Tuesday morning.
# Thank you. I am much closer to understanding clearly. :)
# Here's the improved program. 9 functions - 15 lines of main() code.

import random
import time
import NEMO

number = [0,0,0] #establishes a zero sum for hotdog tally list 
    
# You can change the names of teh contestants here (but Curly needs to win more!)
def contestNames():
    name = ['Moe', 'Larry', 'Curly']
    return name

# allows the user to pick who they think will win
def userPick(name):
    pick = ""
    while not pick in name: # only allows proper input
        pick = NEMO.userString("Who do you think will win? (Moe, Larry, or Curly):")
    return pick

# allows the user to place a bet on the contest - does not allow over betting
def getWager(money):
    wager = NEMO.userInt("How much do you want to wager on this contest? \
(You have $%i):" % money)
    # if user enters too much, the bet is adjusted 
    if wager > money:
        print ("You do not have that much money. I will accept a bet of %i" % money)
        wager = money    
    return wager    

# function that creates a list of three random dogs eaten with different rates 
# so the game is rigged. 'number' will increase through game, 'dogseat' will 
# reset each time this function runs
def sortOfRandDogs(number):
    dogsEat = [0,0,0]
    #Moe's rate 1-4
    #Larry's rate 1-5
    #Curly's rate 1-6 (Best bet is here!)
    for i in range (0, 3):
        dogsEat[i] = random.randrange(1, 5+i)
    for i in range (0, 3):
        number[i] += dogsEat[i]
    return number    

# function that prints the status of how many dogs have been eaten
def printDogStatus(name, number):
    for i in range (0, 3):
        print "%s has eaten %i hot dogs!" % (name[i], number[i])
        i =+ 1
        
# function that determines the winner by comparing maxnumber with list of totals
def determineWinner(name, number):
    winner = ""
    for i in range (0, 3):
        if number[i] == max(number):
            winner = name[i] ###
    return winner

# determines the payout based upon winning or losing updates money
def payOut(winner, pick, money, wager):
    if winner == pick:
        print "\nYou picked the winner, %s." % winner
        money = (money + wager)
    else:
        print "\nYou did not pick the winner, %s." % winner
        money = (money - wager)       
    print "Your total holdings are $%s\n" % money
    return money    
        
# if you go broke you are kicked out, otherwise you loop
def timeToStop(money, number):
    if money == 0:
        print "You are broke and are done here!"
        go = False
    else:
        # resets the number count
        for i in range (0, 3):
            number[i] = 0
        go = True    
    return go        

# this is the main place to mainly be the main    
def main():
    # starting numbers
    money = 100
    number = [0,0,0]
    # start of main loop
    go = True
    while go == True:
        # pulls names of contestants
        name = contestNames()
        # gets input for user's choice of winner
        pick = userPick(name)
        # collects a bet for the contest
        wager = getWager(money)
        # loops the contest until one of the totals clears 50
        while max(number) < 51:
            print "\nnom... nom... nom...\n"
            time.sleep(1)
            # calculates the sort of random increase of hot dogs for each contestant
            number = sortOfRandDogs(number)
            # prints the status of the contestants
            printDogStatus(name, number)
        #having looped, the contest a winner must be determined
        winner = determineWinner(name, number)
        # also amount of the bet is added or subtracted - total offered
        money = payOut(winner, pick, money, wager)
        # program self terminates when you go broke (should add escape command)
        go = timeToStop(money, number)
main()        


