def read_input():
    s1 = input()
    s2 = input()
    return s1, s2


def levenstein(s1, s2):
    I = len(s1) + 1
    J = len(s2) + 1
    dp = [[0] * J for _ in range(I)]
    for i in range(1, I):
        dp[i][0] = i
    for j in range(1, J):
        dp[0][j] = j
    for i in range(1, I):
        for j in range(1, J):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[I - 1][J - 1]


def main():
    print(levenstein(*read_input()))


if __name__ == '__main__':
    main()
