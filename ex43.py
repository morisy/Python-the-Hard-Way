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
        employees = [
                "Suit",
                "Red",
                "Hacker"
        ]
        correct_employee = employees[randint(0,len(employees))]
        print "Here it is, what the long, hellish morning has lead up to:"
        print "Your chance to pitch the buyer, and either make or break"
        print "your company once and for all."
        print "You're supposed to meet with %s" % correct_employee
        print "Let's take a look at your deck:"
        print self.deck
        print "Not bad, hopefully you can make the sale."
        print "But how are you feeling? You'll need all the stamina you can"
        print "muster to out last the intimidating executive in front of you."
        self.print_status()
        print "Well, hope that's good enough!"
        print "Now who were you supposed to meet with again?"
        print "Your phone died last night at the hotel and you're not"
        print "quite sure. The receptionist is out today, but three"
        print "employees walk into the lobby, each looking at you expectantly."
        print "In turn, they are:"
        employee_count = 0
        while employee_count < len(employees):
            print employees[employee_count]
            employee_count += 1
        print "Which one do you follow?"
        action = raw_input("> ")
        if action == correct_employee:
            return "sale_complete"
        else:
            return "leave"
        
    def sale_complete(self):
        print "Wow, you made the sale! Complete victory."
        exit(1)

a_game = Game("lobby")
a_game.play()