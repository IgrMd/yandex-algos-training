def input_read():
    n = int(input())
    sequence_n = [int(x) for x in input().split()]
    m = int(input())
    sequence_m = [int(x) for x in input().split()]
    return n, sequence_n, m, sequence_m


def sub_sequece(n, sequence_n, m, sequence_m):
    answ = []
    if n == 0 or m == 0:
        return answ
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if sequence_m[i] == sequence_n[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if sequence_m[i] == sequence_n[j]:
            answ.append(sequence_n[j])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            assert False
    return answ[::-1]


def main():
    print(*sub_sequece(*input_read()))


if __name__ == '__main__':
    main()
