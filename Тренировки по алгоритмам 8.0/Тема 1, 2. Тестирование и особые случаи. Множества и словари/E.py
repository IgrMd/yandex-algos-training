def read_input():
    n, k = map(int, input().split())
    return n, k


def increment_naive(n, k):
    i = 0
    while i < k:
        n += n % 10
        i += 1
    return n


def increment(n, k):
    i = 0
    while i < k and n % 10 != 2:
        n += n % 10
        if n % 10 == 0:
            return n
        i += 1
    while i + 160 < k:
        n += 800
        i += 160
    while i < k:
        n += n % 10
        i += 1
    return n


def test():
    increment(0, 10000)
    for i in range(10):
        if increment(i, 10000) != increment_naive(i, 10000):
            print(f'{i}: {increment(i, 10000)} != {increment_naive(i, 10000)}')


def main():
    print(increment(*read_input()))


if __name__ == '__main__':
    # test()
    main()
