"""
This is a dictionary for entire words that are commonly
misspelled in leetspeak. One word maps to a list of
possible substitutions.
"""
common_misspellings = {
    "the": ["teh"],
    "my" : ["mah"],
    "hi": ["hai"],
    "own": ["pwn"],
    "youre": ["ur", "u r"],
    "your": ["ur"],
    "you": ["u"],
    "is": ["iz"],
    "its": ["itz"],
    "that": ["taht"],
    "are": ["r"],
    "bye": ["bi", "bai"],
    "cool":["kewl"],
    "mate": ["m8"],
    "please": ["plz", "pl0x"],
    "why": ["y"],
    "what": ["wut"],
    "yeah": ["ya", "yea"],
}

"""
This is a dictionary of common conventions of English that leetspeak
replaces with its own spelling.
"""
phrase_mispellings = {
    "acks": "ax",
    "ack": "ax",
}

"""
These are replacements for suffixes
"""
suffix_replacements = {
    "xer": "xor",
    "or": "zor",
    "ed": "'d",
    "and": "&",
    "anned": "&"
}