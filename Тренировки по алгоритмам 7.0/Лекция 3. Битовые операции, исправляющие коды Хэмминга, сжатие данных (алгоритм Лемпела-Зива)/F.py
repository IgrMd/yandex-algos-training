import sys

EMPTY = 0
POW = 128

for _ in range(POW):
    EMPTY <<= 1
    EMPTY += 1


def rooks_3d():
    n, k = map(int, sys.stdin.readline().split())
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
    for i in range(k):
        x, y, z = map(lambda a: int(a) - 1, sys.stdin.readline().split())
        xy[x][y] = False
        chunk = z // POW
        pos = z % POW
        xz[x][chunk] &= ~(1 << pos)
        yz[y][chunk] &= ~(1 << pos)
    chunk_total = len(xz[0])
    for x in range(n):
        for y in range(n):
            if xy[x][y]:
                for chunk in range(chunk_total):
                    c1 = xz[x][chunk]
                    c2 = yz[y][chunk]
                    if c1 & c2:
                        for z in range(POW):
                            if c1 & c2 & 1:
                                print('NO')
                                print(x + 1, y + 1, POW * chunk + z + 1)
                                return
                            c1 = c1 >> 1
                            c2 = c2 >> 1
    print('YES')


def main():
    rooks_3d()


if __name__ == '__main__':
    main()
