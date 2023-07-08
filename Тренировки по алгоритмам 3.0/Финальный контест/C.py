def read_input():
    n = int(input())
    a, b = [], []
    for _ in range(n):
        a_now, b_now = [int(x) for x in input().split()]
        a.append(a_now)
        b.append(b_now)
    return n, a, b


def couriers(n, a, b):
    t_max = max(sum(a), sum(b))
    INF = t_max + 1
    dp = [[INF] * (t_max + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for t_first_courier in range(t_max + 1):
            dp[i][t_first_courier] = dp[i - 1][t_first_courier] + b[i - 1]
            if t_first_courier >= a[i - 1]:
                dp[i][t_first_courier] = min(dp[i][t_first_courier], dp[i - 1][t_first_courier - a[i - 1]])

    answer = [max(t_first_courier, t_second_courier) for t_first_courier, t_second_courier in enumerate(dp[n])]
    t_first_courier = answer.index(min(answer))
    t_second_courier = dp[n][t_first_courier]
    path = []
    for i in range(n - 1, -1, -1):
        step = -1
        if dp[i][t_first_courier] + b[i] == t_second_courier:
            t_second_courier -= b[i]
            step = 2
        else:
            t_first_courier -= a[i]
            step = 1
        path.append(step)

    return path[::-1]

def main():
    print(*couriers(*read_input()))


if __name__ == '__main__':
    main()
