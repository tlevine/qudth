def length(line):
    start, end = line
    return end - start

def t_test(lines, func = length, conf = 0.95):
    X = list(map(func, lines))
    n = len(X)
    x_bar = sum(X) / n

    return x_bar
