def read_input():
    n = int(input())
    mountains = [0] * (n + 2)
    for i in range(1, n + 1):
        point_x, point_y = [int(x) for x in input().split()]
        mountains[i] = point_y
    m = int(input())
    chains = [[int(x) for x in input().split()] for _ in range(m)]
    return n, mountains, m, chains


def max_climbs(n, mountains, m, chains):
    prefix_sums_direct = [0] * (n + 1)
    for i in range(1, n + 1):
        if mountains[i] - mountains[i - 1] > 0:
            prefix_sums_direct[i] = prefix_sums_direct[i - 1] + mountains[i] - mountains[i - 1]
        else:
            prefix_sums_direct[i] = prefix_sums_direct[i - 1]
    prefix_sums_reversed = [0] * (n + 2)
    for i in range(n, 0, -1):
        if mountains[i] - mountains[i + 1] > 0:
            prefix_sums_reversed[i] = prefix_sums_reversed[i + 1] + mountains[i] - mountains[i + 1]
        else:
            prefix_sums_reversed[i] = prefix_sums_reversed[i + 1]
    for start, end in chains:
        if start > end:
            print(prefix_sums_reversed[end] - prefix_sums_reversed[start])
        else:
            print(prefix_sums_direct[end] - prefix_sums_direct[start])


def main():
    max_climbs(*read_input())


if __name__ == '__main__':
    main()
