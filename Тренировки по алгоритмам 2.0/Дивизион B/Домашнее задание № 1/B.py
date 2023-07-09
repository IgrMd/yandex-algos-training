def read_input():
    n, i, j = [int(x) for x in input().split()]
    return n, i, j


def station_count(n, i, j):
    straight_way = abs(i - j) - 1
    reversed_way = n - max(i, j) + min(i, j) - 1
    return min(straight_way, reversed_way)


def main():
    print(station_count(*read_input()))


if __name__ == '__main__':
    main()
