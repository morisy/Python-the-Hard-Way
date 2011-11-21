class Lexicon(object):

    def __init__(self):
        self.lexicon = {}
        direction = ("north", "south", "east", "west", "down", "up", "left", "right", "back")
        verbs = ("go", "stop", "kill", "eat")
        stop = ("the", "in", "from", "of", "at", "it")
        nouns = ("door", "bear", "princess", "cabinet")

        for i in direction:
            self.lexicon = {"direction": i}
        for i in verbs:
            self.lexicon = {"verbs": i}
        for i in stop:
            self.lexicon = {"stop": i}
        for i in nouns:
            self.lexicon = {"nouns": i}


    def scan(self):
        sentence = self.break_sentence()
        result = []
        for word in sentence:
            if word in self.lexicon:
                result += (self.lexicon[word], word)
            else:
                result += ("error", word)


    def break_sentence(self,):
        words = self.split()
        return words

    def convert_number(self):
        try:
            return int(self)
        except ValueError:
            return None

lexer = Lexicon()
lexer.scan()
