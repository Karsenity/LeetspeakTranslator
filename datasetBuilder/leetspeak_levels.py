"""
Level 1 leetspeak replaces all vowels with simple numbers
"""
def levelOne(sentences):
    v_map = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "u": "u"
    }
    sentences = [s.lower() for s in sentences]
    return ["".join([v_map[ch] if ch in v_map.keys() else ch for ch in s]) for s in sentences]

"""
Level 2 leetspeak builds on leetspeak 1, but also replaces consonants with numbers or 
simple character representations if they exist. Below we only use some of the more common substitutions.
Some characters may not be flipped at all if no easy flip exists.
"""
# TODO: Add additional choices for each character
def levelTwo(sentences):
    sentences = levelOne(sentences)
    c_map = {
        "b": "8",
        "c": "(",
        "d": "|)",
        "f": "f",
        "g": "9",
        "h": "#",
        "j": "j",
        "k": "x",
        "l": "1",
        "m": "m",
        "n": "n",
        "p": "p",
        "q": "0",
        "r": "2",
        "s": "5",
        "t": "7",
        "u": "u",
        "v": "\/",
        "w": "vv",
        "x": "%",
        "y": "y",
        "z": "2"
    }
    return ["".join([c_map[ch] if ch in c_map.keys() else ch for ch in s]) for s in sentences]

# TODO: Implement level 3
def levelThree(sentences):
    return sentences