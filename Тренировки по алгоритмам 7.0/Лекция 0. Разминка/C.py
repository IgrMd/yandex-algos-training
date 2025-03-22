def read_input():
    n = int(input().strip())
    coords = list(map(int, input().split()))
    return n, coords


def nails(n: int, coords: list[int]):
    max_coord = 10 ** 9
    dp = [0] * n
    coords.sort()
    coords.append(max_coord)
    dp[0] = dp[1] = coords[1] - coords[0]
    for i in range(2, n):
        dp[i] = min(dp[i - 2] + coords[i] - coords[i - 1], dp[i - 1] + coords[i + 1] - coords[i])
    return dp[-1]


def main():
    print(nails(*read_input()))


if __name__ == '__main__':
    main()
