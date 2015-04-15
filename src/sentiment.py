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
select r1, r2, r3, r4, r5
from data
where word='%s';
'''


def get_sentiment(string, db_name='sentiment1.db'):
    '''Get the sentiment for a string from the db.
    The string may have multiple words'''

    sentiment = 0

    words = string.strip().split()
    connection = sqlite3.connect(db_name)

    cursor = connection.execute(sum_query)
    totals = cursor.fetchone()

    cursor = connection.execute(sum_query)
    max_occurrences = cursor.fetchone()[0]

    count = 0
    idfs = []
    ratings = []
    entropies = []
    importances = []

    for word in words:
        cursor = connection.execute(query % word)
        result = cursor.fetchone()
        if result:
            occurrences = sum(result)
            average = sum([a*b for a, b in zip(result, range(1, 6))])
                 / occurrences
            ratios = [(100 * float(a)/b)**2 for a, b in zip(result, totals)]
            # print 'ratios', ratios
            # print 'result', result
            # print 'ratios', ratios
            # print 'totals', totals

            ratings.append((average - 3) * 2.5)
            idfs.append(math.log(max_occurrences / sum(result)) + 1)
            entropies.append(entropy.calculate(ratios))

    if len(ratings):
        #print 'entropies', entropies
        dot_product = sum(
            [r*(1-e**10) for r, i, e in zip(ratings, idfs, entropies)])
        rating = dot_product / sum(idfs)
        return rating
    else:
        return 0


def main(db_name='sentiment1.db'):
    '''Compute sentiment based on whatever was piped in'''

    sentiment = 0

    # add sentiment for each line
    for line in sys.stdin:
        sentiment += get_sentiment(line, db_name)
    print 'sentiment(%s): %s' % (line.strip(), sentiment)


if __name__ == '__main__':
    main()
