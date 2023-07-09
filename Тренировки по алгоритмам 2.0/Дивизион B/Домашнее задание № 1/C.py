def read_input():
    x, y, z = [int(x) for x in input().split()]
    return x, y, z


def dates(x, y, z):
    if x == y:
        return 1
    if x <= 12 and y <= 12:
        return 0
    else:
        return 1


def main():
    print(dates(*read_input()))


if __name__ == '__main__':
    main()
