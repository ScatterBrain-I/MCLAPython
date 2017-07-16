import NEMO

# if height is < 54 or age < 14 may not ride
# if height == 54 and age == 14 ask attendant
# if height > 54 and age > 14 may ride

height = NEMO.userInt("Please enter you height in inches:")
age = NEMO.userInt("Please enter your age:")

mayRide = height > 54 and age > 14  # True or False
mayNotRide = height < 54 or age < 14  # True or False
askAttendant = height == 54 and age == 14  # True or False

# ************
# you can just add these into the if statements and not use intermediate variables
# ************

print "(May Ride = %s)" % mayRide
print "(Moy Not Ride = %s)" % mayNotRide
print "(Ask attendant = %s)" % askAttendant
print

if mayRide:  # If it is true you do not need to type "if mayRide == True:"
    print "You may ride!"
elif mayNotRide:
    print "You may not ride."
elif askAttendant:
    print "You must ask Attendant."
else:
    print "Something is wrong with program."