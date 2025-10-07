from bisect import bisect, bisect_right


def read_input():
    n = int(input().strip())
    intervals = [(float('-inf'), float('-inf'), 0)]
    for _ in range(n):
        b, c, w = map(float, input().split())
        intervals.append((b, c, w))
    return n, intervals


BEGIN = 0
END = 1
WEIGHT = 2


def schedule_for_weighted_intervals(n: int, intervals: list[tuple]):
    if n == 0:
        return 0
    if n == 1:
        return intervals[-1][WEIGHT]
    intervals.sort(key=lambda x: (x[END], x[BEGIN]))
    n += 1
    dp = [0] * n
    dp[1] = intervals[1][WEIGHT]

    for i in range(2, n):
        prev = bisect_right(a=intervals, x=intervals[i][BEGIN], lo=0, hi=i, key=lambda x: x[END]) - 1
        dp[i] = max(dp[i - 1], dp[prev] + intervals[i][WEIGHT])
    return dp[-1]


def main():
    print(schedule_for_weighted_intervals(*read_input()))


if __name__ == '__main__':
    main()
