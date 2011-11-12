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

        self.awake = 10
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
        print "Your awake level is %i." % self.awake
        print "Your pee level is %i." % self.pee
        print "You've got $%i left." % self.cash
        if self.awake >= 20:
            print "You're feeling mighty frisky!"
        elif self.awake <= 15:
            print "You really could use an energy boost."
        else:
            print "You're feeling alright, but not quite 100%"
        if self.pee >= 10:
            print "You really have to go!"
        elif self.pee >= 5:
            print "You should probably hit the restroom if you get a chance."
        elif self.pee >= 2:
            print "You might want to hold off on any more beverages until after the pitch."
    def lobby(self):
        employees = [
                "Suit",
                "Red",
                "Hacker"
        ]
        correct_employee = employees[randint(0,len(employees) - 1)]
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
            return "break_room"
        else:
            return "leave"

    def break_room(self):
        print "Phew, you chose wisely."
        print "You follow the person you came to see, and they"
        print "brusquely ask if you want anything to drink. Coffee or tea?"
        print "Feeling slightly tired after fending off man-sized bed bugs"
        print "the night before, you gratefully accept."
        print '"Coffee room is over there. Help yourself."'
        print "You head over into the room and see several carafes, all with"
        print "weird, colorful names but no indication of whether they"
        print "are regular, decaf or half-caff. You desperately need"
        print "a pick-me-up, but drinking too much of the wrong coffee"
        print "will send you to the restroom faster than you can say"
        print "America runs on Dunkin'."
        print "You go to read the labels a little more closely."
        coffee_name_adjective = [
                "Mocha",
                "Iced",
                "Dark",
                "Light",
                "Seasonal",
                "Gutemalan",
                "Spiced",
                "Vanilla"]
        coffee_name_noun = [
                "Roast",
                "Blend",
                "Mix",
                "Brew"]
        carafe_count = 5
        carafe = {}
        while len(carafe) < carafe_count:
                carafe[coffee_name_adjective[randint(0,len(coffee_name_adjective)-1)] + " " + coffee_name_noun[randint(0,len(coffee_name_noun) - 1)]] = randint(0,2)
        print carafe.keys()
        self.print_status()
        print "Which coffee do you want? (Leave to leave)"
        drink = raw_input("> ")
        while drink != "Leave":
            if drink in carafe:
                print "Ah, that was tasty!"
                self.pee += 1
                self.awake += carafe[drink]
            else:
                print "That wasn't an option. Try again."
            self.print_status()
            if self.pee >= 10:
                return 'restroom'
            else:
                print "Another cup?"
                drink = raw_input("> ")
        if self.awake >= 20:
            return "the_pitch"
        else:
            print "You're getting sleepy, veery sleepy ..."
            return 'leave'

    def restroom(self):
        print "Just couldn't hold it together, huh?"
        print "You stumble off to the restroom, losing track of the person you came to see."
        print "When you come back out, it's too late: They're lost in the shuffle."
        return 'leave'

    def sale_complete(self):
        print "Wow, you made the sale! Complete victory."
        exit(1)

    def the_pitch(self):
        prospect_resolve = 20
        print "Your prospect comes back to the break room."
        print "Well, you're looking a bit more up and at 'em"
        print '"Come in to my office."'
        print "Here it is, the moment you've been waiting for."
        print "You look back over at the slides you've been preparing."
        print "Which one do you want to open with?"
        while prospect_resolve > 0 and self.awake > 0:
            if len(self.deck) < 1:
                print "Oh no, you're out of slides!"
                print "You stammer for a few minutes, but it's not doing much good."
                return 'leave' 
            print "Here are your remaining slides:"
            print self.deck
            slide = raw_input("> ")

            if slide in self.deck:
                print "Yup, you have that slide."
                self.deck.remove(slide)
                if slide == "Introduction":
                    if prospect_resolve == 20:
                        print "Did 4 damage to Prospect's Resolve! Critical Hit!"
                        prospect_resolve += -4
                    else:
                        print "Did 1 damage to Prospect's Resolve!"
                        prospect_resolve += -1
                elif slide == "Problem":
                    print "Did 2 damage to Prospect's Resolve!"
                    prospect_resolve += -2
                elif slide == "Buzzwords":
                    print "Did 16 damage to Prospect's Resolve!"
                    prospect_resolve += -16
                else:
                    print "Did 1 Damage to Prospect's Resolve!"
                    prospect_resolve += -1
                self.awake += -1
            else:
                print "Sorry, you don't have that slide."
            self.print_status()
            print "Your prospect has %i resolve left" % prospect_resolve
        if prospect_resolve <= 0:
            return 'sale_complete'
        else:
            return 'leave'
a_game = Game("lobby")
a_game.play()
