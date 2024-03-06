def read_input():
    n = int(input())
    holes = [list(map(int, input().split())) for _ in range(n)]
    return holes


def part_perimeter(holes):
    field = [[1] * 10 for _ in range(10)]
    for x, y in holes:
        field[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    ans = 0
    for x, y in holes:
        for i in range(4):
            ans += field[x + dx[i]][y + dy[i]]
    return ans


def main():
    print(part_perimeter(read_input()))


if __name__ == '__main__':
    main()
