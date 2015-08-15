import argparse
from functools import partial

from sparkprob import sparkprob

from . import sample, aggregate

def qudth(fp, n = None, func = aggregate.length, bins = 20):
    if n:
        get_sample = partial(sample.srs, n)
    else:
        get_sample = sample.census
    X = list(map(func, get_sample(fp)))
    return {
        'min': min(X),
        'max': max(X),
        'mean': aggregate.mean(X),
        'histogram': aggregate.histogram(bins, X),
    }

def main():
    args = argparser.parse_args()
    stats = qudth(args.file)
    places = max(len(str(stats['min'])), len(str(stats['min'])))
    formatstring = '% ' + str(places) + 'd'
    for k in ['min', 'max']:
        stats[k] = formatstring % stats[k]
    stats 
    template_args = {
        'filename': fp.name,

    sys.stdout.write(template % template_args)

argparser = argparse.ArgumentParser('Estimate the length of a line in a file.')
argparser.add_argument('file', type = argparse.FileType('rb'))

template = '''qudth results for %(filename)s

%(histogram)s
%(min)s%(spaces)s%(mean)s%(spaces)s%(max)s
'''
