import sys

sys.setrecursionlimit(100000)


def read_input():
    n = int(input().strip())
    keys = []
    for i in range(n):
        keys.append(int(input().strip()) - 1)
    return n, keys


def piggy_banks(n: int, keys: list[int]):
    colors = [0] * n

    def dfs(cur, color):
        if colors[cur] == -1:
            return -1
        if colors[cur] > 0:
            return colors[cur]
        next = keys[cur]
        colors[cur] = -1
        res = dfs(next, color)
        if res == -1:
            colors[cur] = color
        else:
            colors[cur] = res
        return res

    color = 0
    for i in range(n):
        if not colors[i]:
            color += 1
            dfs(i, color)

    return len(set(colors))


def main():
    print(piggy_banks(*read_input()))


if __name__ == '__main__':
    main()
