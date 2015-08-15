import random

def census(fp):
    lines = set()
    line = None

    while line != '':
        line_start = fp.tell()
        line = fp.readline()
        line_end = fp.tell()
        lines.add((line_start, line_end))

    return lines


def srs(fp, n):
    '''
    If data are appended to the file during the function call,
    the appended data are ignored for the sampling.
    '''
    file_start = fp.tell()
    file_end = fp.seek(0, 2)
    lines = set()
    while len(lines) < n:
        fp.seek(random.randint(file_start, file_end))
        fp.readline()
        line_start = fp.tell()
        fp.readline()
        line_end = fp.tell()
        lines.add((line_start, line_end))
        if line == '':
            break
    fp.seek(file_start)
    return lines
