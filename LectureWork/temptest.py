import random
import time
import NEMO

number = [0,0,0] 
name = ['Moe', 'Larry', 'Curly']

def userPick():
    pick = ""
    while not pick in name: # only allows proper input
        pick = NEMO.userString("Who do you think will win? (Moe, Larry, or Curly):")
    return pick
    
def sortOfRandDogs():
    dogsEat = [0,0,0]
    for i in range (0, 3):
        dogsEat[i] = random.randrange(1, 5+i)
    for i in range (0, 3):
        number[i] += dogsEat[i]
    return number    

def printDogStatus():
    for i in range (0, 3):
        print "%s has eaten %i hot dogs!" % (name[i], number[i])
        i =+ 1

def determineWinner():
    winner = ""
    for i in range (0, 3):
        if number[i] == max(number):
            winner = name[i]
    return winner # IS this where 'winner is? That is grabbed by payOut?

# payout takes three pieces of 9information
# the winner, the user pick, and the current money in the bank
# this allows payout to have what it needs without
# calling functions that have already been called in main
def payOut(winner, pick, money, wager): #i see
    if winner == pick:
        print "\nYou picked the winner, %s." % winner
        money = (money + wager)
    else:
        print "\nYou did not pick the winner, %s." % winner
        money = (money - wager)       
    print "Your total holdings are $%s\n" % money

    if money == 0:
        print "You are broke and are done here!"
        go = False
    else:
        for i in range (0, 3):
            number[i] = 0
        go = True
    return go

def main():
    money = 100
    go = True
    while go == True:
        pick = ""
        while not pick in name: # only allows proper input
            pick = NEMO.userString("Who do you think will win? (Moe, Larry, or Curly):")

        wager = NEMO.userInt("How much do you want to wager on this contest? \
(You have $%i):" % money)

        if wager > money:
            print ("You do not have that much money. I will accept a bet of %i" % money)
            wager = money    

        while max(number) < 51:
            print "\nnom... nom... nom...\n"
            time.sleep(1)
            sortOfRandDogs()
            printDogStatus()
        winner = determineWinner()
        
        # call payout and pass it the winner, user pick, and current money
        # this information can then be used in payout
        # let's take a look at payout
        go = payOut(winner, pick, money, wager) 
        
            
        
main()        


