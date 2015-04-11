#!/usr/bin/python

from decimal import *
import math
import sys

import entropy

def emit(word, occurrences):
    total_occurrences = sum(occurrences)
    total_rating = sum([a*b for a,b in zip(occurrences, range(1,6))])
    average = float(total_rating) / total_occurrences
    print '%s\t%s\t%s\t%s' % (word, average, total_occurrences, entropy.entropy(occurrences))

current_word = None

for line in sys.stdin:
    word, rating, occurences = line.strip().split('\t', 2)
    rating = int(float(rating))
    occurences = int(occurences)
    
    if word != current_word:
        if current_word:
            emit(current_word, occurrence_count)
        
        current_word = word
        occurrence_count = [0] * 5
        doc_count = [0] * 5
    
    occurrence_count[rating - 1] += occurences
    doc_count[rating - 1] += 1  

emit(word, occurrence_count)
