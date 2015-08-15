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
    stats = qudth(args.file, bins = args.bins)

    stat_keys = ['min', 'mean', 'max']

    places = len(str(stats['max']))
    formatstring = '% ' + places + 'd'
    str_stats = {k:(formatstring % (stats[k])) for k in minmax}

    str_stats['delimiter_left'] = int((len(stats['histogram']) - 3 * places) / 2)
    str_stats['delimiter_right'] = len(stats['histogram']) - 3 * places - delimiter_left
    bottom = '%(delimiter_left)s%(min)s%(delimiter_right)s%(max)s' % str_stats

    template_args = {
        'filename': args.file.name,
        'histogram': stats['histogram'],
        'bottom': bottom,
    }
    sys.stdout.write(template % template_args)

argparser = argparse.ArgumentParser('Estimate the length of a line in a file.')
argparser.add_argument('file', type = argparse.FileType('rb'))
argparser.add_argument('--bins', type = int, default = 20)

template = '''qudth results for %(filename)s

%(histogram)s
%(bottom)s
'''
