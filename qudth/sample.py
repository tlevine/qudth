import random

def srs(fp, n):
    '''
    If data are appended to the file during the function call,
    the appended data are ignored for the sampling.
    '''
    file_start = 0
    file_end = fp.seek(0, 2)
    lines = set()
    while len(lines) < n:
        fp.seek(random.randint(file_start, file_end))
        fp.readline()
        line_start = fp.tell()
        fp.readline()
        line_end = fp.tell()
        lines.add((line_start, line_end))
