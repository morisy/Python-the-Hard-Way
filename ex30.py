people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif people > cars:
    "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    "We still can't decide."

if people > buses:
    print "Alright, let's just takes the buses."
else:
    print "Fine, let's stay home then."
