#Give value to string x
x = "There are %d types of people." % 10

#Give value to string binary
binary = "binary"

#Give value to string do_not
do_not = "don't"

#print value of binary and do_not
y = "There who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r. " % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e