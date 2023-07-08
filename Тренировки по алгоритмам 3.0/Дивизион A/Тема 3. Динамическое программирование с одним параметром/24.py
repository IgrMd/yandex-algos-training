def to_seconds(time: str):
    h, m, s = [int(x) for x in time.split(sep=':')]
    m = h * 60 + m
    s = m * 60 + s
    return s


START = to_seconds('09:00:00')
LUNCH = to_seconds('13:00:00')
LUNCH_END = to_seconds('14:00:00')
END = to_seconds('18:00:00')


def read_input():
    n = int(input())
    schedule = []
    for i in range(n):
        time, nail_t = input().split()
        time_s = to_seconds(time)
        nail_t = int(nail_t)
        schedule.append([time, time_s, nail_t])

    times_to_nail = [0] * END
    j = 0
    for i in range(n):
        time_to_nail = schedule[i][2]
        show_end = schedule[i + 1][1] if i < n - 1 else END
        while j < show_end:
            times_to_nail[j] = time_to_nail
            j += 1
    return n, times_to_nail


def nails(n, times_to_nail):
    dp = [0] * (END + 1)
    for i in range(START, END):
        dp[i + 1] = max(dp[i + 1], dp[i])
        if LUNCH <= i < LUNCH_END:
            continue
        if i < LUNCH < i + times_to_nail[i]:
            continue
        if i + times_to_nail[i] > END:
            continue
        dp[i + times_to_nail[i]] = max(dp[i + times_to_nail[i]], dp[i] + 1)

    return dp[END]


def main():
    print(nails(*read_input()))


if __name__ == '__main__':
    main()
