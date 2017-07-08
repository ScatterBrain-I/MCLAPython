print"How many malcorps did you find on planet Exflon?",
malcorps = raw_input()
malcorps = (int(malcorps))
print"How many malcorps did you find on planet Mobiles?",
malcorps = (int(raw_input()) + malcorps)
print"How many malcorps did you find on planet Monsantoes?",
malcorps = (int(raw_input()) + malcorps)

print "You found %s malcorps!" % malcorps
print "The average malcorps per planet is %.2f." % (malcorps / 3.0)