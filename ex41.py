from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
            "Nice job. You died ... jackass.",
            "Such a luser.",
            "I have a small puppy that's better at this."]

    print quips[randint(0, len(quips)-1)]
    exit(1)

def central_corridor():
    print "The Gothons of Planet Cape have invaded your ship and destroyed your crew."
    print "The Gothons of Planet Percal #25 have invaded your ship and destroyed your"
    print "entire crew. You are the last surviving member and your last mission is to"
    print "get the neutron destruct bomb from the Weapons Armory, put it in the"
    print "bridge, and blow the ship up after getting into an escape pod.You're"
    print "running down the central corridor to the Weapons Armory when a Gothon jumps"
    print "out red scaly skin, dark grimy teeth, and evil clown costume flowing"
    print "around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you."

    action = raw_input("> ")

    if action == "shoot!":
        print "Quick on the draw you yank out your blaster and fire it at the Gothon."
        print "His clown costume is flowing and moving around his body, which throws off your aim."
        print "You miss, ruining his costume and ticking him off."
        print "He shoots you repeatedly in the face. Ouch!"
        return 'death'
    
    elif action == "dodge!":
        print "You should've kept up with your pilates. You dodge about as fast"
        print "as spit freezes in the Sahara, and take that laser like a champ."
        return 'death'
    elif action == "tell a joke":
        print "Bwa. Bwaha. Bwahahaha!"
        print "The Gothon laughs incontrollably, giving you a chance to grab his pistol, aim carefully, a send him back to the bronze age."
        return 'laser_weapon_armory'
    else:
        print "Does not compute!"
        return 'central_corridor'

def laser_weapon_armory():
    print "Welcome to the armory."
    print "Guess the 3-digit key code for the bomb!"
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    guess = raw_input("[keypad]> ")
    guesses = 0

    while guess != code and guesses < 10:
        print "BZZZZEEEED!"
        guesses += 1
        guess = raw_input("[keypad]> ")

    if guess == code:
        print "Ch-Ching! You're in. You grab the bomb and make a dash to the bridge."
        return 'the_bridge'
    else:
        print "Oops, that wasn't the right code."
        return 'death'

def the_bridge():
    print "Uh oh, 5 more Gothons are after you."

    action = raw_input("> ")

    if action == "Throw the bomb":
        print "In a panic, you throw the bomb ... and it detonates, killing you along with your mortal enemies."
        return 'death'

    elif action == "Slowly place the bomb":
        print "Tick tick tick ... You manage to get to the escape bay by freaking them out."
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE!"
        return 'the_bridge'

def escape_pod():
    print "You make it to the escape bay, but there's 5 pods to choose from. Which is best?"
    good_pod = radint(1,5)
    guess = raw_input("[pod #]> ")

    if int(guess) != good_pod:
        print "Uh oh ... Pod %d has a broken thruster. It's going to be a tough ri--" % guess
        return 'death'
    else:
        print "Phew ... You got a working pod! You win!"
        exit(0)

ROOMS = {
        'death': death,
        'central_corridor': central_corridor,
        'laser_weapon_armory': laser_weapon_armory,
        'the_bridge': the_bridge,
        'escape_pod': escape_pod
}

def runner(map, start):
    next = start
    while True:
        room = map[next]
        print "\n----------------------"
        next = room()

runner(ROOMS, 'central_corridor')
