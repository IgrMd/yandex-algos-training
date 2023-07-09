def read_input():
    n = int(input())
    coordinates = [int(x) for x in input().split()]
    return n, coordinates


def summary_way(y, coordinates):
    way = 0
    for coordinate in coordinates:
        way += abs(y - coordinate)
    return way


def school_coordinate(n, coordinates: list):
    ways = [0] * n
    ways[0] = summary_way(coordinates[0], coordinates)
    for i in range(1, n):
        delta = coordinates[i] - coordinates[i - 1]
        ways[i] = ways[i - 1] + i * delta - (n - i) * delta
    min_way = ways[0]
    coord = coordinates[0]
    for i in range(n):
        if ways[i] < min_way:
            min_way = ways[i]
            coord = coordinates[i]
    return coord


def main():
    print(school_coordinate(*read_input()))


if __name__ == '__main__':
    main()
