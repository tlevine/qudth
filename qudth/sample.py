import random

def census(fp):
    lines = []
    line = None

    while line != b'':
        line_start = fp.tell()
        line = fp.readline()
        line_end = fp.tell()
        lines.append((line_start, line_end))

    return lines


def srs(n, fp):
    '''
    with replacement

    If data are appended to the file during the function call,
    the appended data are ignored for the sampling.
    '''
    file_start = fp.tell()
    file_end = fp.seek(0, 2)
    lines = []

    while len(lines) < n:
        fp.seek(random.randint(file_start, file_end))
        fp.readline()
        line_start = fp.tell()
        line = fp.readline()
        line_end = fp.tell()
        if line == b'':
            pass
        elif line[-1] == 10: # newline
            lines.append((line_start, line_end))
        else:
            raise NotImplementedError('I can\'t handle this line:\n%s' % line)

    fp.seek(file_start)
    return lines
