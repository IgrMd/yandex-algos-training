def read_input():
    n, m = [int(x) for x in input().split()]
    return n, m


def paths(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for diagonal in range(1, max(n, m) + min(n, m) - 1):
        i = diagonal if diagonal < n else n - 1
        j = 0 if diagonal < n else diagonal - n + 1
        while i >= 0 and j < min(diagonal + 1, m):
            way1 = dp[i - 2][j - 1] if i > 1 and j > 0 else 0
            way2 = dp[i - 1][j - 2] if i > 0 and j > 1 else 0
            way3 = dp[i + 1][j - 2] if i + 1 < n and j > 1 else 0
            way4 = dp[i - 2][j + 1] if i > 1 and j + 1 < m else 0
            dp[i][j] = way1 + way2 + way3 + way4
            i -= (1 if i > 0 else 0)
            j += (1 if j < m else 0)
    return dp[-1][-1]



assert paths(4, 4) == 2
assert paths(2, 3) == 1
assert paths(3, 2) == 1
assert paths(1, 1) == 1
assert paths(2, 2) == 0

def main():
    print(paths(*read_input()))


if __name__ == '__main__':
    main()
