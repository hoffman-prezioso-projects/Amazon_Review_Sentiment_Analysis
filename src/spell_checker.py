#!/usr/bin/env python
import os


class SpellChecker:
    dictionary = {}

    def __init__(self):
        self.dictionary = {}
        current_directory = os.path.dirname(os.path.abspath(__file__))
        word_list = open(current_directory + "/en_dictionary.txt", 'r')

        for word in word_list:
            self.dictionary[word.strip()] = True

    def check(self, word):
        try:
            self.dictionary[word.lower()]  # throws KeyError if word not found

            # word in dictionary
            return True

        except:  # word not in dictionary
            return False
