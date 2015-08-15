import argparse

from .qudth import qudth

def cli():
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
