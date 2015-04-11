#!/usr/bin/env python

import math
import sqlite3
import sys

query = '''
select rating, occurrences * 1.0 / total.max as df, entropy
from data
, (select max(occurrences) as max
	from data) as total
where word='%s';
'''

def get_sentiment(string, db_name = 'sentiment.db'):
    '''Get the sentiment for a string from the db.
    The string may have multiple words'''
    
    sentiment = 0
    
    words = string.strip().split()
    connection = sqlite3.connect(db_name)
    
    count = 0
    idfs = []
    ratings = []
    entropies = []
    importances = []
    
    for word in words:
        cursor = connection.execute(query % word)
        result = cursor.fetchone()
        if result:
            ratings.append((result[0] - 3) * 2.5)
            idfs.append(math.log(1.0 / result[1], 2) + 1)
            entropies.append(result[2])
            importances.append(result[1] / (0.1 + 0.9 * result[2]))
            #idfs.append(math.log(1.0 / result[1]) + 1)

    if len(ratings):
        dot_product = sum([r*i*(1-e) for r,i,e in zip(ratings, idfs, entropies)])
        rating = dot_product / sum(idfs)
        return rating;
    else:
        return 0

def main(db_name = 'sentiment.db'):
    '''Compute sentiment based on whatever was piped in'''
    
    sentiment = 0

    value = ''

    # add sentiment for each line
    for line in sys.stdin:
        line = line.strip()
        value += line + ' '
        sentiment += get_sentiment(line, db_name)
    
    if len(value) > 30:
        value = value[:30] + '...'
    else:
        value = value[:-1]
    print 'sentiment(%s): %s' % (value, sentiment)


if __name__ == '__main__':
    main();
