#!/usr/bin/python

from decimal import *
import sys


def emit(word, occurrence_counts):
    '''
    Outputs word and occurence counts for each rating, tab delimited.
    Sample format "dog    10    123    222    435    736"
    '''

    count_output = []

    for rating_count in occurrence_counts:
        count_output.append(str(rating_count))

    count_output = '\t'.join(count_output)

    print '%s\t%s' % (word, count_output)


current_word = None

for line in sys.stdin:
    word, rating, occurrences = line.strip().split('\t', 2)
    rating = int(float(rating))
    occurrences = int(occurrences)

    if word != current_word:
        if current_word:
            emit(current_word, occurrence_counts)

        current_word = word
        occurrence_counts = [0] * 5

    occurrence_counts[rating - 1] += occurrences

emit(word, occurrence_counts)
