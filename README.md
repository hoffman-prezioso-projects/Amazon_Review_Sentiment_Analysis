# Sentiment Analysis using Amazon Reviews
## Overview
Using a [corpus of 34.6 million Amazon reviews](http://snap.stanford.edu/data/web-Amazon.html) collected by Jure Leskovec over 18 years, we created a sentiment dictionary containing 97,436 unique words that correspond to a zero-centered floating point sentiment score.
## Process
We first preprocessed the data from the corpus to remove extraneous information. We only used the review text and the rating star value of each review. After preprocessing, we used MapReduce to compute the frequency for each word in each star rating 1 through 5. After obtaining the frequencies of each word, we wrote a sentiment algorithm to compute the sentiment score of each word.

## Results
### Positive Words
| Word | Sentiment Score |
|---|---|
| good | 0.152603809091 |
| great | 3.78021467713 |
| awesome | 6.8840020218 |
| amazing | 6.54080771437 |
| perfect | 5.78771983374 |
| exceptional | 5.72747983897 |
| wonderful | 6.05087919002 |
| best | 3.2653374328 |

### Negative Words
| Word | Sentiment Score |
|---|---|
| bad | -5.03251524289 |
| terrible | -8.97044440118 |
| awful | -10.0215084233 |
| trash | -9.3655215103 |
| garbage | -10.1554413225 | 
| hate | -1.79682763912 |
| worst | -9.94203065622 |

### Neutral Words
| Word | Sentiment Score |
|---|---|
| a | 0.0125160264947 |
| the | 0.00423728459134 |
| it | -0.0294755274737 |
| and | 0.0810574365028 |
| an | 0.0318918766949 |
| or | -0.274298468178 |
| average | -1.20676256035 |
| normal | -0.0270787859177 |

