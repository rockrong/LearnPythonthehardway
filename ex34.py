animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def PrintAnimal(index):
    if index == 1:
        num2en = "1st"
    elif index == 2:
        num2en = "2nd"
    elif index == 3:
        num2en = "3rd"
    else:
        num2en = str(index)+'th'
    print "The %s animal is at %d and is a %s" % (num2en, index - 1, animals[index - 1])
    print "The animal at %d is the %s animal and is a %s" % (index - 1, num2en, animals[index - 1])

for i in range(1,7):
    PrintAnimal(i)
