# Sentiment Analysis using Amazon Reviews
## Overview
Using a [corpus of 34.6 million Amazon reviews](http://snap.stanford.edu/data/web-Amazon.html) collected by Jure Leskovec over 18 years, we created a sentiment dictionary containing 97,436 unique words that correspond to a zero-centered floating point sentiment score.
## Process
We first preprocessed the data from the corpus to remove extraneous information. We only used the review text and the rating star value of each review. After preprocessing, we used MapReduce to compute the frequency for each word in each star rating 1 through 5. After obtaining the frequencies of each word, we wrote a sentiment algorithm to compute the sentiment score of each word.

## Results

