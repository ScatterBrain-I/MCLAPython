import random
import NEMO

def main():
    ans = random.randrange(1,11)
    keepGoing = True
    count = 1
    while keepGoing:
        guess = NEMO.userInt("Enter a guess from 1 to 10:")
        if guess > ans:
            print "Too high"
        elif guess < ans:
            print "Too low."
        elif guess == ans:
            print "You win!"
            print "It took you %s guesses." % count
            keepGoing = False
        else:
            print "That is not a valid entry. Try again."
        count += 1    
main()
