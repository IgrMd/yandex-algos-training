def input_read():
    n = int(input())
    return n


def operations(n):
    n_max = 10 ** 7
    dp = [0] * (n + 3)
    prev = [0] * (n + 3)
    dp[2], dp[3] = 1, 1
    prev[2], prev[3] = 1, 1
    for x in range(4, n + 1):
        n_plus1 = dp[x - 1]
        n_mul2 = dp[x // 2] if x % 2 == 0 else n_max
        n_mul3 = dp[x // 3] if x % 3 == 0 else n_max
        n_min = min(n_plus1, n_mul2, n_mul3)
        if n_min == n_plus1:
            dp[x] = dp[x - 1] + 1
            prev[x] = x - 1
        elif n_min == n_mul2:
            dp[x] = dp[x // 2] + 1
            prev[x] = x // 2
        elif n_min == n_mul3:
            dp[x] = dp[x // 3] + 1
            prev[x] = x // 3
    numbers = [n]
    i = n
    while i != 1:
        numbers.append(prev[i])
        i = prev[i]
    return dp[n], numbers


def main():
    count, numbers = operations(input_read())
    print(count)
    print(*numbers[::-1])


if __name__ == '__main__':
    main()
