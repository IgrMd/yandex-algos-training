def read_input():
    n = int(input().strip())
    ratings = [int(x) for x in input().split()]
    return n, ratings


def average_level(n, ratings):
    prefix_sum = [0] * n
    prefix_sum[0] = ratings[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + ratings[i]
    discontent_levels = [0] * n
    for i in range(n):
        discontent_levels[i] = abs(prefix_sum[i] - (i + 1) * ratings[i]) + abs(
            ratings[i] * (n - i - 1) - (prefix_sum[-1] - prefix_sum[i]))
    return discontent_levels


def main():
    print(*average_level(*read_input()))


if __name__ == '__main__':
    main()
