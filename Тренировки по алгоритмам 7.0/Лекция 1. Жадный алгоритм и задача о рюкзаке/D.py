def read_input():
    n, m = map(int, input().split())
    mi = list(map(int, input().split()))
    return n, m, mi


def backpack(n: int, m: int, mi: list[int]):
    dp = [False] * (m + 1)
    dp[0] = True
    for m_i in mi:
        i = m - m_i
        while i >= 0:
            if dp[i]:
                dp[i + m_i] = True
            i -= 1
    for i in range(m, -1, -1):
        if dp[i]:
            return i
    return 0


def main():
    print(backpack(*read_input()))


if __name__ == '__main__':
    main()
