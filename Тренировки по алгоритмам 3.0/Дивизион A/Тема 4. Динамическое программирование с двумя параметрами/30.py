def read_input():
    length, n = [int(x) for x in input().split()]
    wood = [0]
    wood += [int(x) for x in input().split()]
    wood.append(length)
    return wood, n, length


def wood_cut(wood, n, length):
    N = n + 2
    dp = [[0] * N for _ in range(N)]
    max_cost = length ** 2
    for diagonal in range(N + 1, 2 * N - 1):
        l = 2 * (N - 1) - diagonal if diagonal >= N - 1 else N - 1
        r = diagonal if diagonal < N - 1 else N - 1
        while l >= 0 and r >= max(0, diagonal - N + 1):
            min_cost = max_cost if r - l > 1 else 0
            for i in range(l + 1, r):
                cost = dp[l][i] + dp[i][r]
                if cost < min_cost:
                    min_cost = cost
            dp[l][r] = wood[r] - wood[l] + min_cost
            l -= 1
            r -= 1
    return dp[0][-1]


def main():
    print(wood_cut(*read_input()))


if __name__ == '__main__':
    main()
