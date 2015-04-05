#!/usr/bin/env python

import sqlite3
import sys

def get_sentiment(string, db_name):
  '''Get the sentiment for a string from the db.
  The string may have multiple words'''
  
  sentiment = 0
  
  words = string.strip().split()
  connection = sqlite3.connect(db_name)
  
  for word in words:
    cursor = connection.execute('SELECT sentiment FROM data WHERE word="%s";' % word)
    result = cursor.fetchone()
    if result:
      sentiment += result[0]

  return sentiment


def main(db_name = 'sentiment.db'):
  '''Compute sentiment based on whatever was piped in'''
  
  sentiment = 0

  # add sentiment for each line
  for line in sys.stdin:
    sentiment += get_sentiment(line, db_name)
  print 'sentiment: %s' % (sentiment)


if __name__ == '__main__':
  main();
