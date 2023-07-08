def input_read():
    n = int(input())
    cost = [0] * (n + 1)
    for i in range(1, n + 1):
        cost[i] = int(input())
    return n, cost


def lunches(n, cost):
    max_cost = 10 ** 6
    dp = [[max_cost for j in range(n + 1)] for i in range(n + 1)]
    dp[0][0] = 0
    prev = [[[0, 0] for j in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n + 1):
            for_coupon = dp[i - 1][j + 1] if j < n else max_cost
            if cost[i] > 100:
                coupon_granted = 1
                for_money = dp[i - 1][j - 1] + cost[i]
            else:
                for_money = dp[i - 1][j] + cost[i]
                coupon_granted = 0
            if for_coupon < for_money:
                coupon_granted = -1
                dp[i][j] = for_coupon
                prev[i][j][0] = j + 1
            else:
                dp[i][j] = for_money
                prev[i][j][0] = j - 1 if coupon_granted else j
            prev[i][j][1] = coupon_granted
    min_cost = max_cost
    coupons_left = n
    for j, value in enumerate(dp[-1]):
        if value <= min_cost:
            min_cost = value
            coupons_left = j
    i = n
    j = coupons_left
    days_coupon_spent = []
    coupons_spent = 0
    while i > 0:
        if prev[i][j][1] == -1:
            days_coupon_spent.append(i)
            coupons_spent += 1
        j = prev[i][j][0]
        i -= 1
    return min(dp[n]), coupons_left, coupons_spent, days_coupon_spent[::-1]


def main():
    min_cost, coupons_left, coupons_spent, days_coupon_spent = lunches(*input_read())
    print(min_cost)
    print(coupons_left, coupons_spent)
    print(*days_coupon_spent)


if __name__ == '__main__':
    main()
