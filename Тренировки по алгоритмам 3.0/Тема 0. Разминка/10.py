from collections import defaultdict


def read_input():
    k = int(input())
    return k


def fill(dictionary, s, i, j):
    for k in range(i, j):
        dictionary[s[k]] += 1


def solve(s):
    result = defaultdict(int)
    size = len(s)
    for i, c in enumerate(s, 1):
        result[c] += i * (size - i + 1)
    result = sorted(result.items())
    for c, n in result:
        print(f'{c}: {n}')


def main():
    solve(input())


if __name__ == '__main__':
    main()
