#!/usr/bin/python

from decimal import *
import math
import sys

#import entropy

def emit(word, occurrences):
    #total_occurrences = sum(occurrences)
    #total_rating = sum([a*b for a,b in zip(occurrences, range(1,6))])
    #average = float(total_rating) / total_occurrences
    #print '%s\t%s\t%s\t%s' % (word, average, total_occurrences, entropy.entropy(occurrences))
    print '%s\t%s' % (word, '\t'.join(str(x) for x in occurrences))

current_word = None

reviews = [0] * 5

for line in sys.stdin:
    word, rating, occurrences = line.strip().split('\t', 2)
    rating = int(float(rating))
    occurrences = int(occurrences)
    
    reviews[rating - 1] += occurrences

    if word != current_word:
        if current_word:
            emit(current_word, occurrence_count)
        
        current_word = word
        occurrence_count = [0] * 5
        doc_count = [0] * 5
    
    occurrence_count[rating - 1] += occurrences
    doc_count[rating - 1] += 1  

emit(word, occurrence_count)

for i in range(len(reviews)):
    print >> sys.stderr, reviews
