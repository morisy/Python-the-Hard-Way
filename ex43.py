from sys import exit
from random import randint

class Game(object):
    def __init__(self, start):
        self.deck = [
                "Introduction",
                 "Problem",
                "Closing",
                "Flow Chart",
                "Buzzwords"
        ]

        self.resolve = 30
        self.awake = 1
        self.pee = 0
        self.cash = 200
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n======================="
            room = getattr(self, next)
            next = room()

    def leave(self):
        print "You're clearly not cut out for the big leagues."
        print "Head on home to your lemonade stand and practice."
        exit(1)

    def print_status(self):
        print "You're feeling mighty frisky!"

    def lobby(self):
        print "Here it is, what the long, hellish morning has lead up to:"
        print "Your chance to pitch the buyer, and either make or break"
        print "your company once and for all."
        print "Let's take a look at your deck:"
        print self.deck
        print "Not bad, hopefully you can make the sale."
        print "But how are you feeling? You'll need all the stamina you can"
        print "muster to out last the intimidating executive in front of you."
        self.print_status()
        print "Well, hope that's good enough!"
        return 'leave'



a_game = Game("lobby")
a_game.play()
