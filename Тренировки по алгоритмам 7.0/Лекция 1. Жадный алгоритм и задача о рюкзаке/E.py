def read_input():
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    return n, m, weights, costs


def backpack(n: int, m: int, weights: list[int], costs: list[int]):
    dp = [-1] * (m + 1)
    dp[0] = 0
    for i in range(n):
        weight = weights[i]
        cost = costs[i]
        curr_weight = m - weight
        while curr_weight >= 0:
            if dp[curr_weight] != -1:
                dp[curr_weight + weight] = max(dp[curr_weight + weight], dp[curr_weight] + cost)
            curr_weight -= 1
    return max(dp)


def main():
    print(backpack(*read_input()))


if __name__ == '__main__':
    main()
