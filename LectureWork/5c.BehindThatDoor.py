import random
import NEMO
import time

def main():
    
    # initialize prizes
    good_prizes = ["A New Car!", "$100", "A Badge in Python Class", "A Free A!"]
    bad_prizes = ["An Old Sock", "A Smelly Garbage Can", "A Sore Throat", "More Homework" ]
    
    #create a list for teh doors
    doors = ["","",""]
    
    #place random bad prizes behind all 3 doors
    random.shuffle(bad_prizes)
    doors[0] = bad_prizes[0]
    doors[1] = bad_prizes[1]
    doors[2] = bad_prizes[2]
    
    #replace one door with a good prize
    random.shuffle(good_prizes)
    iGoodPrize = random.randrange(0,3)
    doors[iGoodPrize] = good_prizes[0]
    door = NEMO.userInt("Pick a door:")
    print "You win..."
    time.sleep(3)
    print "%s" % doors[door-1]
    print doors
    
main()    