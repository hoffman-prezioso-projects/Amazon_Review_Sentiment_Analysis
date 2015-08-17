# Sentiment Analysis using Amazon Reviews
## Overview
Using a [corpus of 34.6 million Amazon reviews](http://snap.stanford.edu/data/web-Amazon.html) collected by Jure Leskovec over 18 years, we created a sentiment dictionary containing 97,436 unique words that correspond to a zero-centered floating point sentiment score.
## Process
With the corpus, we first preprocessed the data to remove extraneous information that was not being used. We only used the review text and the rating value of each review. After preprocessing the data, we used MapReduce to get a usage count for each word in each rating 1 through 5. After obtaining the usage counts, we created a sentiment algorithm to compute the sentiment score of each word.

