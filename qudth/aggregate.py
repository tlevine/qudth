from itertools import repeat

def length(line):
    start, end = line
    return end - start

def histogram(bins, X):
    _min = min(X)
    _bucketsize = (max(X) - _min) / float(bins)
    buckets = list(repeat(0, bins))
    for x in X:
        buckets[int((x - _min) / _bucketsize)] += 1
    return buckets

def mean(X):
    return sum(X) / len(X)
