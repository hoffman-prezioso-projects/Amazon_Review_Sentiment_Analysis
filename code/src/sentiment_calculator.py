#!/usr/bin/env python

import sqlite3
import numpy


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


def get_total_sentiment(rows, total_rating_counts):
    """
    Takes list of database rows and returns the sentiment of the phrase.
    Database row is of form [word, r1, r2, r3, r4, r4].
    r1 corresponds to the total ratings of 1 star reviews.
    r2 corresponds to 2 star reviews.
    etc.
    """

    phrase_sentiment = 0

    for word_row in rows:
        word = word_row[0]
        rating_totals = word_row[1:]

        word_sentiment = algorithm(rating_totals, total_rating_counts)
        phrase_sentiment += word_sentiment

    return phrase_sentiment


def map_multiply_and_sum(rating_totals):
    """Multiplies each rating total by (rating - 3) and sums.
    1 star is mapped to -2
    2 stars is mapped to -1
    3 stars is mapped to 0
    4 stars is mapped to 1
    5 stars is mapped to 2
    """

    sentiment = 0
    multipliers = range(-2, 3)
    for index, multiplier in enumerate(multipliers):
        sentiment += rating_totals[index] * multiplier

    return sentiment


def normalize_totals(rating_totals, total_rating_counts):
    """
    First divides each rating total for a specific word by the
    total number of ratings for a given star value.
    Then, with the remaining values, find the maximum and normalize
    using the maximum.
    """

    normalized_rating_totals = [0] * 5

    for star_value in range(0, 5):
        normalized_rating_totals[star_value] = \
            float(rating_totals[star_value]) / total_rating_counts[star_value]

    max_value = max(normalized_rating_totals)

    for i in range(0, 5):
        normalized_rating_totals[i] /= max_value

    return normalized_rating_totals


def correction_factor(sentiment):
    """Apply a shift and multiplier to correct sentiment values."""

    shift = 0
    multiplier = 40
    corrected_sentiment = (sentiment * multiplier) + shift

    return corrected_sentiment


def algorithm(rating_totals, total_rating_counts):
    """
    Normalize Rating Totals
    Map, Muliply, and Sum
    Apply Correction Value
    Multiply by Standard Deviation Squared
    """

    normalized_rating_totals = normalize_totals(rating_totals,
                                                total_rating_counts)

    normalized_sum = map_multiply_and_sum(normalized_rating_totals)
    corrected_sentiment = correction_factor(normalized_sum)
    standard_deviation = numpy.std(normalized_rating_totals)
    sentiment = corrected_sentiment * (standard_deviation**2)

    return sentiment


def print_calculation_info(rows, total_rating_counts):
    """Displays information and values about each word"""

    for word_row in rows:
        word = word_row[0]
        rating_totals = word_row[1:]

        normalized_totals = normalize_totals(rating_totals,
                                             total_rating_counts)
        normalized_sum = map_multiply_and_sum(normalized_totals)

        print "\n"
        print "Word: ", word
        print "Rating Totals: ", rating_totals
        print "Normalized Totals: ", normalized_totals
        print "Normalized Basic Sum: ", normalized_sum
        print "Corrected Sentiment: ", correction_factor(normalized_sum)
        print "Standard Deviation**2: ", \
            (numpy.std(normalize_totals(rating_totals,
                                        total_rating_counts)))**2

        print "\n"


def get_total_rating_counts(cursor):
    """Calculate sum of total ratings for each rating value."""

    total_rating_counts = [0] * 5

    for star_value in range(1, 6):
        star_column = "r" + str(star_value)
        cursor.execute('SELECT SUM(' + star_column + ') FROM data')
        line = cursor.fetchone()
        total_rating_counts[star_value - 1] = line[0]

    return total_rating_counts


def main(db_name='sentiment.db'):
    conn = sqlite3.connect(db_name)
    conn.text_factory = str
    cursor = conn.cursor()

    total_rating_counts = get_total_rating_counts(cursor)
    print "Type -q to quit."

    while True:
        phrase = raw_input(":> ").lower().strip()
        if phrase == "-q":
            break
        words = phrase.split()

        rows = get_database_rows(words, cursor)
        sentiment = get_total_sentiment(rows, total_rating_counts)

        # Print individual word information
        # print_calculation_info(rows, total_rating_counts)

        print "Phrase: ", phrase
        print "Total Sentiment: ", sentiment

    conn.close()
    print "Goodbye"


if __name__ == '__main__':
    main()
