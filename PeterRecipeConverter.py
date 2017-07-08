# Program by Peter Niemeyer 2017/07/07
# MCLA Python / Mark Cohen

# This program:
# 1. inquires several amounts of ingredients for a bread recipe
# 2. offers weight equivalents for ingredients
# 3. inquires for a multiplying factor
# 4. offers new ingredients amounts with weights for use in scaled up recipe
#     (Apologies for changing the appearance of output from assignment example. 
#     I hope this is not a concern.)

# Magic numbers
flourwgt = 110.0     # grams per cup
waterwgt = 236.59    # grams per cup
saltwgt = 5.0        # grams per teaspoon
yeastwgt = 2.83      # grams per teaspoon

# 1 & 2: inputs for 4 basic ingredients along with output of weight equivalent
print "-- Original Recipe --"
print "Enter the amount of Flour (cups):",
flour = raw_input()
print "(That is %.0f grams of well sifted flour.)" % (float(flour) * flourwgt) 
print
print "Enter the amount of water (cups):",
water = raw_input()
print "(That is %.0f grams of water.)" % (float(water) * waterwgt)
print
print "Enter the amount of salt (teaspoons):",
salt = raw_input()
print "(That is %.0f grams of table salt.)" % (float(salt) * saltwgt)
print
print "Enter the amount of yeast (teaspoons):",
yeast = raw_input()
print "(That is %.0f grams of baker's yeast.)" % (float(yeast) * yeastwgt)
print

# 3. Inquery for a multiplier to scale the recipe
print "Enter the loaf adjustment factor (e.g. 2.0 double the size):",
adjustment = raw_input() 
print

# 4. Out put of scaled recipe along with weights for more precice bakers
print "-- Modified Recipe --"
print "Flour: %.2f cups." % (float(flour) * float(adjustment)),
print "(That is %.2f grams of well sifted flour.)" % (float(flour) * flourwgt * float(adjustment))
print "Water: %.2f cups." % (float(water) * float(adjustment)),
print "(That is %.2f grams of water.)" % (float(water) * waterwgt * float(adjustment))
print "Salt: %.2f teaspoons." % (float(salt) * float(adjustment)),
print "(That is %.2f grams of table salt.)" % (float(salt) * saltwgt * float(adjustment))
print "Yeast: %.2f teaspoons." % (float(yeast) * float(adjustment)),
print "(That is %.2f grams of baker's yeast.)" % (float(yeast) * yeastwgt * float(adjustment))
print "Happy Baking!"