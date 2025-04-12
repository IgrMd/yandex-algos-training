from dataclasses import dataclass


@dataclass
class Brick:
    l: int
    c: int


def read_input():
    n, k = map(int, input().split())
    bricks = [Brick(*map(int, input().split())) for _ in range(n)]
    return n, k, bricks


def two_walls(n: int, k: int, bricks: list[Brick]):
    wall_size = 0
    for brick in bricks:
        if brick.c == 1:
            wall_size += brick.l
        brick.c -= 1

    wall: list[list] = [[None] * (wall_size + 1) for _ in range(k)]
    for row in wall:
        row[0] = 0
    for i, brick in enumerate(bricks):
        row = wall[brick.c]
        for l in range(wall_size - brick.l, -1, -1):
            if row[l] is not None:
                if not row[l + brick.l]:
                    row[l + brick.l] = i + 1
    div_l = 0
    for i in range(1, wall_size):
        flag = True
        for row in wall:
            flag &= bool(row[i])
        if flag:
            div_l = i
            break
    if not div_l:
        print('NO')
        return
    ans = []
    for row in wall:
        l = div_l
        while l > 0:
            brick_i = row[l]
            ans.append(brick_i)
            brick_i -= 1
            l -= bricks[brick_i].l
    # ans.sort()
    print('YES')
    print(*ans, sep='\n')


def main():
    two_walls(*read_input())


if __name__ == '__main__':
    main()
