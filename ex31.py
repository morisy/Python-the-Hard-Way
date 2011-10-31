print "You enter a dark room with two doors. Do you go through Door #1 or Door #2?"

prompt = "> " 
door = raw_input(prompt)

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Yell at the bear?"

    bear = raw_input(prompt)

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the abyss into Cthuhlu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    insanity = raw_input(prompt)

    if insanity == 1 or insanity == 2:
        print "Your body survives powered by a brain of jello."
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
else:
    print "You stumble around and fall on a knife and die. Good job!"
