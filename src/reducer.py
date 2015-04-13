#!/usr/bin/python

from decimal import *
import sys


def emit(word, occurrence_counts):
    print '%s\t%s' % (word, '\t'.join(str(x) for x in occurrence_counts))

current_word = None
review_total_counts = [0] * 5

for line in sys.stdin:
    word, rating, occurrences = line.strip().split('\t', 2)
    rating = int(rating)
    occurrences = int(occurrences)

    review_total_counts[rating - 1] += occurrences

    if word != current_word:
        if current_word:
            emit(current_word, occurrence_counts)

        current_word = word
        occurrence_counts = [0] * 5

    occurrence_counts[rating - 1] += occurrences

emit(word, occurrence_counts)
