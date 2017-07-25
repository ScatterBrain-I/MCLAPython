import random
import NEMO
print random.randrange(1,5)

def main():
    ans = random.randrange(1,11)
    keepGoing = True
    while keepGoing:
        guess = NEMO.userInt("Enter a guess from 1 to 10:")
        if guess == ans:
            print "You win!"
            keepGoing = False
main()
