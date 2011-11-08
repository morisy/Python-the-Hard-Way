from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
                "You died. You kinda suck at this.",
                "Your mom would be proud. If she was smarter.",
                "Such a luser.",
                "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "n\==========="
            room = getattr(self, next)
            next = room()

    def death(self):
        next = self.start

        while True:
            room = getattr(self, next)
            next = room()

    def central_corridor(self):
        print "The Gothons of Somerville have invaded your ship and destroyed"
        print "your whole crew. You are now the last hope for humanity: It is"
        print "up to you to grab the Gothon Bomb and use it against them."
        print "Go now: SAVE HUMANITY!"
        print "\nYou're running down the central corridor when you come across"
        print "your first challenge: A hungry, sweaty Gothon, in full clown"
        print "garb ... Do you shoot, dodge, or joke?"

        action = raw_input("> ")

        if action == "shoot":
            print "You put on your John Wayne face, draw your blaster and aim,"
            print "narrowly missing by a hair. Unfortunately, close only"
            print "counts in horseshoes and hand grenades."
            print "The Gothon Frenemey pulls out his own blaster and chortles"
            print "you back to last week."
            return 'death'

        elif action == "dodge":
            print "Zing! Zang! That's what it sounded like in your head."
            print "Unfortunately, you forgot to tie your shoeleaces this"
            print "morning, and you trip, fall and knock yourself out."
            print "Good thing, too, because the Gothon's teeth would've"
            print "reall hurt as they gnawed through your meat-neck."
            return 'death'

        elif action == "joke":
            print "\"So, you heard the one about the Gothon, the Krzyg,"
            print "and the Lzzzzzwiwiwig that walked into a wormhole?\""
            print "Fortunately, he hadn't, and he laughed for a good 10 minutes,"
            print "Giving you a good opportunity to slip through the next door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUETE!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "Excellent, you made it into the bomb room."
        print "Less excellent, there's a coded lock protecting"
        print "it, totalling three devilish digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "BZZZD!"
            if guesses == 3:
                print "You find a scrap of paper."
                print "It says, 'Hey Jim, the new code is "
                print "%s [scratched out]" % code[:2]
                print "Don't lose it this time!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        
        if guess == code:
            print "Ka-Ching! You're in. You grab the bomb,"
            print "high-five yourself and then sprint to the bridge to finish"
            print "off the baddies."
            return 'the_bridge'

        else:
            print "Bzz. Times up, unfortunately. You didn't guess right,"
            print "but judging from your brain matter floating in the void"
            print "of space, it doesn't bother you too much."
            return 'death'

    def the_bridge(self):
        print "You burst onto the bridge, confronted by 4 more Gorthon scum."
        print "Do you throw or place the bomb?"

        action = raw_input("> ")

        if action == "throw":
            print "Well, that seemed like a good idea ... until the Gothons"
            print "shoot you as soon as the bomb leaves your hand."
            return 'death'

        elif action == "place":
            print "Your pysche-out attempt works: They stare at the bomb,"
            print "even as it ticks away. You get away to the escape pod bay."
            return "escape_pod"

        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

    def escape_pod(self):
        print "You rush through the ship, the 'tick tick' of the bomb"
        print "echoing in your ears. You make it to the escape pod bay."
        print "There's 5 pods: Which one do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "Unfortunately, it ejects you. Into space."
            return 'death'
        else:
            print "You escape, the baddies ship blowing up behind you."
            print "Good work!"
            exit(0)

a_game = Game("central_corridor")
a_game.play()
