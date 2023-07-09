def read_input():
    a, b, c, d = [int(input()) for _ in range(4)]
    return a, b, c, d


def equation(a, b, c, d):
    if a == 0 and b != 0:
        return 'NO'
    if a == b == 0:
        if c == d == 0:
            return 'NO'
        else:
            return 'INF'
    x = -b // a
    if a * x + b != 0:
        return 'NO'
    if c * x + d == 0:
        return 'NO'
    return x


def main():
    print(equation(*read_input()))


if __name__ == '__main__':
    main()
