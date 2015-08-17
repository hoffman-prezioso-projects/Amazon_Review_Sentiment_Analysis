#!/usr/bin/env python

import math
import sqlite3
import sys

import entropy

sum_query = '''
SELECT SUM(r1) AS sum1
, SUM(r2) AS sum2
, SUM(r3) AS sum3
, SUM(r4) AS sum4
, SUM(r5) AS sum5
FROM data
;
'''

max_query = '''
SELECT MAX(r1 + r2 + r3 + r4 + r5)
FROM DATA;
'''

query = '''
SELECT r1, r2, r3, r4, r5
FROM data
WHERE word='%s';
'''

def get_sentiment(string, db_name='sentiment.db'):
    '''Get the sentiment for a string from the db.
    The string may have multiple words'''

    sentiment = 0

    words = string.strip().split()
    connection = sqlite3.connect(db_name)

    cursor = connection.execute(sum_query)
    totals = cursor.fetchone()
    max_occurrence = max(totals)

    cursor = connection.execute(max_query)
    max_occurrences = cursor.fetchone()[0]

    count = 0
    ratings = []
    entropies = []
    importances = []

    for word in words:
        cursor = connection.execute(query % word)
        result = cursor.fetchone()
        if result:
            ratios = [float(r) / t for r, t in zip(result, totals)]
            exaggerated_ratios = [a**4 for a in ratios]
            average = sum([a*b for a, b in zip(ratios, range(1, 6))]) / float(sum(ratios))
            
            # put rating into the range of -5 to 5
            ratings.append((average - 3) * 2.5)

            # get normalized shannon entropy of frequency squared
            entropies.append(entropy.calculate(exaggerated_ratios))

    if len(ratings):
        dot_product = sum(
            [r*(1-e**10) for r, e in zip(ratings, entropies)])
        rating = dot_product
        return rating
    else:
        return 0


def main(db_name='sentiment.db'):
    '''Compute sentiment based on whatever was piped in'''

    sentiment = 0

    # add sentiment for each line
    for line in sys.stdin:
        sentiment += get_sentiment(line, db_name)
    print 'sentiment(%s): %s' % (line.strip(), sentiment)


if __name__ == '__main__':
    main()
