#!/usr/bin/env python

import math
import sqlite3
import sys

query = '''
select rating, occurrences * 1.0 / total.sum
from data
, (select sum(occurrences) as sum
	from data) as total
where word='%s';
'''

def get_sentiment(string, db_name):
    '''Get the sentiment for a string from the db.
    The string may have multiple words'''
    
    sentiment = 0
    
    words = string.strip().split()
    connection = sqlite3.connect(db_name)
    
    count = 0
    idfs = []
    ratings = []
    for word in words:
        cursor = connection.execute(query % word)
        result = cursor.fetchone()
        if result:
            ratings.append(result[0])
            idfs.append(math.log(1.0 / result[1]) + 1)

    if len(ratings):
        dot_product = sum([a*b for a,b in zip(ratings, idfs)])
        rating = dot_product / sum(idfs)
        return (rating - 3) * 2.5;
        #return rating * 2 - 5.0
    else:
        return 0

def main(db_name = 'sentiment.db'):
    '''Compute sentiment based on whatever was piped in'''
    
    sentiment = 0

    # add sentiment for each line
    for line in sys.stdin:
        sentiment += get_sentiment(line, db_name)
    print 'sentiment: %s' % (sentiment)


if __name__ == '__main__':
    main();
