import NEMO
def main():
    keepGoing = True
    while keepGoing:
        msg = NEMO.userString("Enter a message (enter exit to quit):")
        if msg == "exit":
            keepGoing = False
        else:
            print msg
main()
