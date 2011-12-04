'''
A couple of tuples are what we use to store words.
'''
directions = ('north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def scan(thewords):
    sentence = thewords.split()
    parsed_sentence = []
    for word in sentence:
        if word in directions:
            parsed_sentence.append(('direction', word))
    return parsed_sentence
