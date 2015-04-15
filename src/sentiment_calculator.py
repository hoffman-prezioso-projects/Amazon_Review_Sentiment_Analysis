#!/usr/bin/env python

import math
import sqlite3
import sys
import entropy
import numpy
from math import log
from decimal import *


def entropy(values, b=0):
    """Return the normalized Shannon entropy of values."""

    if b == 0:
        b = len(values)

    entropy = 0
    total = sum(values)

    for x in values:
        if x > 0:
            ratio = float(x) / total
            entropy -= ratio * log(ratio, b)

    return entropy


def get_database_rows(words, cursor):
	"""Takes list of words and returns list of database data for each word."""

	rows = []
	for word in words:
		cursor.execute('select * from data where word=?', (word, ))
		line = cursor.fetchone()

		if line is None:
			continue
		else:
			line = list(line)
			rows.append(line)
	return rows


def get_total_sentiment(rows):
	"""
	Takes list of database rows and returns the sentiment of the phrase.
	Database row is of form [word, r1, r2, r3, r4, r4].
	r1 corresponds to the total ratings of 1 star reviews.
	r2 corresponds to 2 star reviews.
	etc.
	"""

	scores = []
	phrase_sentiment = 0

	for word_row in rows:
		word = word_row[0]
		rating_totals = word_row[1:]

		word_sentiment = algorithm(rating_totals)
		phrase_sentiment += word_sentiment

	return phrase_sentiment


def basic_sum(rating_totals):
	"""Multiplies each rating total by (rating - 3) and sums"""

	sentiment = 0
	for i, multiplier in enumerate(range(-2, 3)):
		sentiment += rating_totals[i] * multiplier

	return sentiment


def normalize_totals(rating_totals):
	max_total = max(rating_totals)
	normalized_totals = [float(total) / max_total for total in rating_totals]
	return normalized_totals

def algorithm(rating_totals):
	"""Placeholder for better algorithm calculation"""

	sentiment = basic_sum(rating_totals)
	return sentiment


def print_calculation_info(rows):
	"""Displays information and values about each word"""

	for word_row in rows:
		word = word_row[0]
		rating_totals = word_row[1:]

		basic_sum_value = basic_sum(rating_totals)
		entropy_value = entropy(rating_totals)
		normalized_totals = normalize_totals(rating_totals)
		normalized_sum = basic_sum(normalized_totals)
		print "\n"
		print "Word: ", word
		print "Rating Totals: ", rating_totals
		print "Normalized Totals: ", normalized_totals
		print "Basic Sum: ", basic_sum_value
		print "Normalized Basic Sum: ", normalized_sum
		print "Entropy:", entropy_value
		print "\n"


def main(db_name='sentiment.db'):
	conn = sqlite3.connect(db_name)
	conn.text_factory = str
	cursor = conn.cursor()

	while True:
		print "Type -q to quit."
		phrase = raw_input(":>").lower().strip()
		if phrase == "-q":
			break
		words = phrase.split()

		rows = get_database_rows(words, cursor)
		sentiment = get_total_sentiment(rows)

		print_calculation_info(rows)  # Comment out to disable individual word information

		print "Phrase: ", phrase
		print "Total Sentiment: ", sentiment

	conn.close()
	print "Goodbye"


if __name__ == '__main__':
    main()
