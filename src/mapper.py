#!/usr/bin/env python

from decimal import *
import re
import sys

splitter = re.compile('\s+')
nonword_pattern = re.compile(r'[^a-zA-Z]')

def get_word_freq(text):
    word_freq = {};
    max_term_freq = 0
    words = splitter.split(text)
    for word in words:
        word = word.lower()
        if word != '':
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
            if word_freq[word] > max_term_freq:
                max_term_freq = word_freq[word]
    return word_freq, max_term_freq, len(words)


def emit(words, review, source):
    word_freq, max_term_freq, num_words = get_word_freq(words)
    for word in word_freq:
        count = word_freq[word]
        print '%s\t%s\t%s' % (word, review['review/score'], count)


review = {}

for line in sys.stdin:
    
    line = line.strip()
    try: 
        key, value = line.split(': ', 1)
    except ValueError:
        continue

    if key == 'product/productId':
        review = {}

    review[key] = value

    if key == 'review/summary':
        words = re.sub(nonword_pattern, ' ', value)
        emit(words, review, 'summary')

    '''elif key == 'review/text':
        words = re.sub(nonword_pattern, ' ', value)
        emit(words, review, 'text')'''
        


