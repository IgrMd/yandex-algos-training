import math


def transparency(n: int, d: int, trees: set):
    r = int(math.sqrt(d))
    dxy = set()
    y = r
    for x in range(r + 1):
        while x * x + y * y > d and y >= 0:
            y -= 1
        if x * x + y * y == d:
            dxy.add((x, y))
            dxy.add((-x, y))
            dxy.add((x, -y))
            dxy.add((-x, -y))
    ans = 0
    for x, y in trees:
        for dx, dy in dxy:
            if (x + dx, y + dy) in trees:
                ans += 1

    return ans // 2


def main():
    n, d = map(int, input().split())
    trees = set()
    for _ in range(n):
        x, y = map(int, input().split())
        trees.add((x, y))
    print(transparency(n, d, trees))


if __name__ == '__main__':
    main()
