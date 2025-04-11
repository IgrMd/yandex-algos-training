def read_input():
    m = int(input().strip())
    arr = list(map(int, input().split()))
    return m, arr


def internet(m: int, a: list[int]):
    dp = [0] * 31
    dp[0] = a[0]
    for i in range(1, 31):
        if dp[i - 1] >= m:
            dp[i] = dp[i - 1]
        else:
            dp[i] = max(dp[i - 1] * 2, a[i])

    def min_cost(x: int):
        if x == 0:
            return 0
        i = 0
        while x > dp[i]:
            i += 1
        if i == 0:
            return 1
        mem = min(2 ** i, 2 ** (i - 1) + min_cost(x - dp[i - 1]))
        return mem

    return min_cost(m)




def main():
    print(internet(*read_input()))


if __name__ == '__main__':
    main()
