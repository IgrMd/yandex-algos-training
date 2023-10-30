def read_input():
    a, b, c, d = [int(x) for x in input().split()]
    return a, b, c, d


def sum_rationals(l, r, seq):
    now = seq[l]
    for elem in seq[l:r + 1]:
        if elem < now:
            return now
        if elem > now:
            return elem
    return None


def min_in_range(a, b, c, d):
    m, n = a * d + b * c, b * d
    div = 2
    while div <= m and div <= n:
        if n % div == 0 and m % div == 0:
            n = n // div
            m = m // div
            continue
        div += 1
    return m, n


def main():
    print(*min_in_range(*read_input()))


if __name__ == '__main__':
    main()
