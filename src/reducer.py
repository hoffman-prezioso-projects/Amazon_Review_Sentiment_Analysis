#!/usr/bin/python

from decimal import *
import math
import sys

#def emit(word, rating, count, sum_tf_for_rating, source):
#    print '%s\t%s\t%s\t%s\t%s' % (word, rating, count, sum_tf_for_rating, source)

def emit(word, occurrences, doc_count):
    total_occurrences = sum(occurrences)
    total_rating = sum([a*b for a,b in zip(occurrences, range(1,6))])
    print '%s\t%s\t%s' % (word, float(total_rating) / total_occurrences, total_occurrences)
    #for i in range(5):    
    #    if doc_count[i]:
    #        print '%s\t%s\t%s\t%s' % (word, i + 1, occurrences[i], doc_count[i])

current_word = None

for line in sys.stdin:
    word, rating, occurences = line.strip().split('\t', 2)
    rating = int(float(rating))
    occurences = int(occurences)
    #tf = Decimal(tf)
    
    if word != current_word:
        if current_word:
            #print '%s\t%s' % (current_word, float(total) / count)
            emit(current_word, occurrence_count, doc_count)
            '''for i in range(5):
                if sum_tf[i]:
                    emit(current_word, i + 1, count[i], sum_tf[i], source)'''
        
        current_word = word
        #count = [0] * 5
        #sum_tf = [0] * 5
        occurrence_count = [0] * 5
        doc_count = [0] * 5
    
    occurrence_count[rating - 1] += occurences
    doc_count[rating - 1] += 1  
    #sum_tf[rating - 1] += tf
    #count[rating - 1] += occurences

emit(word, occurrence_count, doc_count)
#emit(current_word, i + 1, count[i], sum_tf[i], source)
