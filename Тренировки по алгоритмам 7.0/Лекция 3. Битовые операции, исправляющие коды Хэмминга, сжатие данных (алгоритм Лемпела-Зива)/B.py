def read_input():
    n = int(input().strip())
    m = [list(map(int, input().split())) for _ in range(n)]
    return n, m


def jedi(n: int, m: list[list[int]]):
    ans = [0] * n
    for k in range(n):
        for i in range(n):
            ans[k] |= m[i][k]
        for j in range(n):
            ans[k] |= m[k][j]

    return ans


def main():
    print(*jedi(*read_input()))


if __name__ == '__main__':
    main()
