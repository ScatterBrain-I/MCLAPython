x = 5
y = '7'
print "(%s + %s) = %s" % (x, y, x*y)

s1 = "Hello"
s2 = "Peter"
print s1 + " " + s2
print s1 * x

print "What is your name?",
name = raw_input()
print "%s, your name is %s characters long." % (name, len(name))

s3 = "Python is boring!"
print s3
s4 = s3.replace('boring', 'awesome')
print s4
print s4[3]
print "Python" in s4
print 'dog' in s4

print "Please enter a word:",
word = raw_input()
print "Please enter a nunber:",
number = raw_input()
print "I am the great repeater -- watch this! %s" % (word * int(number))