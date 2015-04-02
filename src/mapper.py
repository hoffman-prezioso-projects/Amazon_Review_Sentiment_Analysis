#!/usr/bin/env python

import re
import sys

splitter = re.compile('\s')

def get_word_freq(text):
	word_req = {};
	words = splitter.split(text)
	for word in words:
		if word in word_req:
			word_req[word] += 1
		else:
			word_req[word] = 1
	return word_req

review = {}

for line in sys.stdin:
	
	line = line.strip()
	key, value = line.split(': ', 1)

	review[key] = value

	if key == 'review/text':
		word_freq = get_word_freq(value)
		for word in word_freq:
			print '%s\t%s,%s' % (word, review['review/score'], word_freq[word])
		review = {}


