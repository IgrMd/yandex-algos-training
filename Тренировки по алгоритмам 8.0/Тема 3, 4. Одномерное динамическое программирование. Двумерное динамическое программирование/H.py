def read_input():
    n = int(input())
    return n


ME = 0
HIM = 1


def matches(n: int):
    count = max(5, n + 1)
    dp = [['B', 'B'] for _ in range(count)]
    dp[1][ME] = dp[0][HIM] = 'W'
    dp[1][HIM] = dp[0][ME] = 'L'
    for i in range(2, count):
        if dp[i][0] == 'B':
            for j in range(i + i, count, i):
                dp[j][ME] = dp[j][HIM] = ''
    for i in range(4, count):
        if dp[i][ME] == 'B':
            continue
        w_count, l_count = 0, 0
        for j in range(1, 4):
            if dp[i - j][ME] == 'B':
                continue
            w_count += dp[i - j][HIM] == 'W'
            l_count += dp[i - j][ME] == 'L'
        dp[i][ME] = 'W' if w_count else 'L'
        dp[i][HIM] = 'L' if l_count else 'W'
    w_count, l_count = 0, 0
    for j in range(1, 4):
        if dp[n - j][ME] == 'B':
            continue
        w_count += dp[n - j][HIM] == 'W'
    dp[n][ME] = 'W' if w_count else 'L'
    return 1 if dp[n][ME] == 'W' else 2


def main():
    print(matches(read_input()))


if __name__ == '__main__':
    main()
