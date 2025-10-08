def read_input():
    n, k = map(int, input().split())
    blocks = [int(x) for x in input().split()]
    return n, k, blocks


INDEX = 0
VAL = 1


def tower(n: int, k: int, blocks: list[int]):
    if n == k:
        return [1]
    if k == 1:
        return [i + 1 for i in range(n)]
    protections = [0] * n
    for i in range(n - k + 1):
        cur_sum = sum(blocks[i:i + k])
        cur_min = min(blocks[i:i + k])
        protections[i] = cur_sum * cur_min
    # dp = [(-1, -1)] * (n + 1)
    dp = [(-1, 0)] * n
    dp[0] = (-1, protections[0])
    for i in range(1, n - k + 1):
        saved_max = 0
        saved_i = -1
        for j in range(0, i - k + 1):
            if dp[j][VAL] > saved_max:
                saved_max = dp[j][VAL]
                saved_i = j
        dp[i] = (saved_i, saved_max + protections[i])

    saved_max = 0
    curr_i = 0
    for i in range(0, n):
        if dp[i][VAL] > saved_max:
            saved_max = dp[i][VAL]
            curr_i = i
    ans = []
    while curr_i != -1:
        ans.append(curr_i + 1)
        curr_i = dp[curr_i][INDEX]
    ans.reverse()
    return ans


def main():
    ans = tower(*read_input())
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
