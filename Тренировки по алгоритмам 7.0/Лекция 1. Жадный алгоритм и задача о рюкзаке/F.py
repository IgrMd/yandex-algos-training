def read_input():
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    return n, m, weights, costs


def backpack(n: int, m: int, weights: list[int], costs: list[int]):
    data = [(0, 0)]
    for i in range(n):
        data.append((costs[i], weights[i]))
    dp: list[list] = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = (0, 0)
    for item in range(1, n + 1):
        dp[item] = dp[item - 1].copy()
        row = dp[item]
        cost, weight = data[item]
        for w_i in range(m - weight, -1, -1):
            if dp[item][w_i] is None:
                continue
            pos_cost = dp[item][w_i][0] + cost
            if row[w_i + weight] is None or row[w_i + weight][0] < pos_cost:
                row[w_i + weight] = (pos_cost, item)
    col = 0
    max_cost = 0
    row = dp[-1]
    for i in range(m + 1):
        if not row[i]:
            continue
        cost, _ = row[i]
        if cost > max_cost:
            max_cost = cost
            col = i

    ans = []
    _, item = dp[-1][col]
    while item > 0:
        ans.append(item)
        col -= data[item][1]
        _, item = dp[item - 1][col]

    return reversed(ans)


def main():
    print(*backpack(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
