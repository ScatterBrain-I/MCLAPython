import NEMO
    
kmweekday = NEMO.userFloat("How many km did you travel on a weekday?")
kmweekend = NEMO.userFloat("How many km did you travel on a weekend?")

miweekday = NEMO.kmToMi(kmweekday)
miweekend = NEMO.kmToMi(kmweekend)

dollarsweekday = miweekday * .13
dollarsweekend = miweekend * .24

print "Weekday $%.2f" % dollarsweekday
print "Weekend $%.2f" % dollarsweekend
print "Total $%.2f" % (dollarsweekday + dollarsweekend)
