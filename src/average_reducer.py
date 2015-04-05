#!/usr/bin/python

import math
import sys

if not sys.argv[1]:
  print "Please supply warc.gz file"
  sys.exit(1)

num_documents = int(sys.argv[1])

def emit(word, average, document_count):
  idf = math.log(num_documents / float(document_count))
  print '%s\t%s' % (word, idf * average)

current_word = None
count = 0
document_count = 0
total = 0

for line in sys.stdin:
  word, rating, ntf, frequency = line.strip().split('\t', 3)
  rating = float(rating) - 2.5
  ntf = float(ntf)
  frequency = int(frequency)
  if word != current_word:
    if current_word:
      emit(current_word, total / count, document_count)
    
    current_word = word
    count = 0
    document_count = 0
    total = 0
  
  count += frequency
  document_count += 1
  total += ntf * rating

emit(current_word, total / count, document_count)
