
from math import log

def entropy(values, b=0):
    '''Return the normalized Shannon entropy of values'''

    if b == 0:
        b = len(values)

    entropy = 0
    total = sum(values)
    
    for x in values:
        if x > 0:
            ratio = float(x) / total
            entropy -= ratio * log(ratio, b)

    return entropy

