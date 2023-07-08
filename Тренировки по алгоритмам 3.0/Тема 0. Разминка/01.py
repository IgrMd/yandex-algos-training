import sys
from collections import defaultdict


def read_input():
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    return lst_in


def prepair_bar(count, max_count):
    return ['#' if i < count else ' ' for i in range(max_count)]


def get_lines(lst):
    chars = defaultdict(int)
    for line in lst:
        for c in line:
            chars[c] += 1
    if ' ' in chars:
        chars.pop(' ')
    max_count = max(chars.values())
    chars = dict(sorted(chars.items()))
    result = []
    for char, count in chars.items():
        line = [char, *prepair_bar(count, max_count)]
        result.append(line)
    result = list(zip(*result))
    result.reverse()
    return result


def main():
    for line in get_lines(read_input()):
        print(*line, sep='')


if __name__ == '__main__':
    main()
