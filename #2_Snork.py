print "Please enter your sentence:",
sen = raw_input()
enc = sen.replace ("a", str(len(sen)))
enc = enc.replace ("e", str((len(sen)+1)))
enc = enc.replace ("i", str((len(sen)+2)))
enc = enc.replace ("o", str((len(sen)+3)))
enc = enc.replace ("u", str((len(sen)+4)))
print enc
dec = sen.replace (str(len(sen)), "a")
dec = dec.replace (str((len(sen)+1)), "e")
dec = dec.replace (str((len(sen)+2)), "i")
dec = dec.replace (str((len(sen)+3)), "o")
dec = dec.replace (str((len(sen)+4)), "u")
print dec

# I was not effecient with my use of len(sen) - Mark made variable for length and used that. Better.