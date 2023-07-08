def read_input():
    n, m, k = [int(x) for x in input().split()]
    mines = [[int(x) for x in input().split()] for _ in range(k)]
    return n, m, k, mines


def render_field(n, m, k, mines):
    field = [[0] * (m + 2) for _ in range(n + 2)]
    neibs_x = [0, -1, -1, -1, 0, 1, 1, 1]
    neibs_y = [-1, -1, 0, 1, 1, 1, 0, -1]
    for x, y in mines:
        for k in range(8):
            neib_x = x + neibs_x[k]
            neib_y = y + neibs_y[k]
            field[neib_x][neib_y] += 1
    for x, y in mines:
        field[x][y] = '*'

    return field


def main():
    field = render_field(*read_input())
    for line in field[1:-1]:
        print(*line[1:-1])


if __name__ == '__main__':
    main()
