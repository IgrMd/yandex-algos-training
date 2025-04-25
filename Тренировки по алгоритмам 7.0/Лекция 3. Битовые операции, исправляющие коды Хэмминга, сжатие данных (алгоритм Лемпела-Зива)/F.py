import sys
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int


EMPTY = 0xFFFF_FFFF
POW = 64


def read_input():
    n, k = map(int, sys.stdin.readline().split())
    rooks = []
    for i in range(k):
        x, y, z = map(int, sys.stdin.readline().split())
        rooks.append(Point(x - 1, y - 1, z - 1))
    return n, rooks


def rooks_3d(n: int, rooks: list[Point]):
    chunk_cnt = n // POW
    rest = 0
    for _ in range(n % POW):
        rest = rest << 1
        rest |= 1
    xy = [[True] * n for _ in range(n)]
    xz = [[EMPTY] * chunk_cnt for _ in range(n)]
    yz = [[EMPTY] * chunk_cnt for _ in range(n)]
    if rest:
        for row in xz:
            row.append(rest)
        for row in yz:
            row.append(rest)
    for p in rooks:
        xy[p.x][p.y] = False
        chunk = p.z // POW
        pos = p.z % POW
        xz[p.x][chunk] &= ~(1 << pos)
        yz[p.y][chunk] &= ~(1 << pos)
    chunk_total = len(xz[0])
    for x in range(n):
        for y in range(n):
            if xy[x][y]:
                for chunk in range(chunk_total):
                    if xz[x][chunk] != 0 and yz[y][chunk] != 0:
                        for z in range(POW):
                            if xz[x][chunk] & (1 << z) and yz[y][chunk] & (1 << z):
                                return x + 1, y + 1, POW * chunk + z + 1

    return None


def main():
    ans = rooks_3d(*read_input())
    if not ans:
        print('YES')
    else:
        print('NO')
        print(*ans)


if __name__ == '__main__':
    main()
