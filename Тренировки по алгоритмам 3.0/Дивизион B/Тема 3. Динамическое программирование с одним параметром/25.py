def input_read():
    n = int(input())
    nails = [int(x) for x in input().split()]
    return n, nails


def rope(n, nails: list):
    max_coord = 10 ** 9
    nails.append(max_coord)
    nails.sort()
    dp = [0] * n
    dp[0] = nails[1] - nails[0]
    dp[1] = dp[0]
    for i in range(2, n):
        dp[i] = min(nails[i] - nails[i-1] + dp[i-2], nails[i+1] - nails[i] + dp[i-1])
    return dp[-1]



def main():
    print(rope(*input_read()))


if __name__ == '__main__':
    main()
