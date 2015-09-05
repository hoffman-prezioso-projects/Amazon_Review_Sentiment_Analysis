#!/usr/bin/env python

import sentiment_calculator as sc
import sqlite3
import sys

def main(db_name='sentiment.db'):
    conn = sqlite3.connect(db_name)
    conn.text_factory = str
    cursor = conn.cursor()
    create_dictionary(cursor)

def get_all_rows(cursor):
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    if not rows:
        sys.exit(1) 
    return rows

def get_word_and_sentiment(db_row, total_counts):
    word = db_row[0]
    word_counts = db_row[1:]
    return word, sc.algorithm(word_counts, total_counts)

def create_dictionary(cursor):
    rows = get_all_rows(cursor)
    total_counts = sc.get_total_rating_counts(cursor)

    for line in rows:
        word, sentiment = get_word_and_sentiment(line, total_counts)
        print "{0},{1}".format(word, sentiment)

if __name__ == '__main__':
    main()
