'''
A couple of tuples are what we use to store words.
'''
directions = ('north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'from', 'at', 'of', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def scan(thewords):
    sentence = thewords.split()
    parsed_sentence = []
    for word in sentence:
        if word in directions:
            parsed_sentence.append(('direction', word))
        elif word in verbs:
            parsed_sentence.append(('verb', word))
        elif word in stops:
            parsed_sentence.append(('stop', word))
        elif word in nouns:
            parsed_sentence.append(('noun', word))
        elif convert_number(word) != None:
            parsed_sentence.append(('number', word))
        else:
            parsed_sentence.append(('error', word))
    return parsed_sentence

def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None
