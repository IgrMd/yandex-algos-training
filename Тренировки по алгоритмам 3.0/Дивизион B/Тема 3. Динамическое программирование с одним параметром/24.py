def input_read():
    n = int(input())
    customers = [[int(x) for x in input().split()] for _ in range(1, n + 1)]
    return n, customers


def quick_buy(n, customers):
    t_max = 10 ** 5
    dp = [0] * (n)
    for i in range(2):
        customers.append([t_max, t_max, t_max])
        dp.append(t_max)
    dp.append(0)
    customers.append([0, 0, 0])
    for i in range(n):
        t_a = customers[i][0] + dp[i - 1]
        t_b = customers[i - 1][1] + dp[i - 2]
        t_c = customers[i - 2][2] + dp[i - 3]
        dp[i] = min(t_a, t_b, t_c)
    return dp[n-1]


def main():
    print(quick_buy(*input_read()))


if __name__ == '__main__':
    main()
