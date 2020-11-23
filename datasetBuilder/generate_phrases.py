"""
Use "dialogs.txt" to get English sentences
Only the first column is used, as the second column
commonly contains what will be said in the following rows
first column.
"""

import random
from datasetBuilder.morphs import phrase_dictionaries
from datasetBuilder.leetspeak_levels import *


class GeneratePhrases:

    def __init__(self, filepath):
        sentences = self.extract_sentences(filepath)
        sentences = self.remove_punctuation(sentences)
        sentences = self.create_misspellings(sentences)
        sentences = self.replace_substrings(sentences)
        self.sentences = self.replace_suffixes(sentences)


    def extract_sentences(self, filepath):
        with open(filepath) as file:
            # Only save the first sentence
            sentences = [line.split("\t")[0] for line in file.readlines()]
        return sentences


    def remove_punctuation(self, sentences):
        """
        Removes uncommon punctuation """
        punc = ["'", "-"]
        return [''.join([ch for ch in sentence if ch not in punc]) for sentence in sentences]


    def create_misspellings(self, sentences):
        mutations = phrase_dictionaries.common_misspellings
        return [" ".join([mutations[word][random.randint(0,len(mutations[word])-1)] if word in mutations.keys() else word for word in s.split()]) for s in sentences]


    def replace_substrings(self, sentences):
        subs = phrase_dictionaries.phrase_mispellings
        retval = []
        for s in sentences:
            for k in subs.keys():
                s = s.replace(k, subs[k])
            retval += [s]
        return retval


    def replace_suffixes(self, sentences):
        subs = phrase_dictionaries.suffix_replacements
        retval = []
        for s in sentences:
            for suffix in subs.keys():
                s = s.replace(suffix + " ", subs[suffix] + " ")
            retval.append(s)
        return retval


    def apply_leetspeak(self, level):
        variations = {
            1: levelOne,
            2: levelTwo,
            3: levelThree
        }
        return variations[level](self.sentences)

#

# Perform character-substitution for alphabetical characters

