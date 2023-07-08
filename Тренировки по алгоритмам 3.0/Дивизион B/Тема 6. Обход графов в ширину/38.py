def input_read():
    n, m, s, t, q = [int(x) for x in input().split()]
    s -= 1
    t -= 1
    fleas = [[int(x) - 1 for x in input().split()] for _ in range(q)]
    return n, m, s, t, q, fleas


def get_field(n, m, s, t, q, fleas):
    field = [[None] * m for _ in range(n)]
    for x, y in fleas:
        field[x][y] = -1
    field[s][t] = 0
    return field


def bfs_fleas(n, m, s, t, q, field):
    distances = [[[s, t]]]
    distance = 0
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    while distance < len(distances):
        for now_x, now_y in distances[distance]:
            distance = field[now_x][now_y] + 1
            for i in range(8):
                x = now_x + dx[i]
                y = now_y + dy[i]
                if x < 0 or x >= n:
                    continue
                if y < 0 or y >= m:
                    continue
                if field[x][y] is None or field[x][y] == -1:
                    field[x][y] = distance
                    if distance >= len(distances):
                        distances.append([])
                    distances[distance].append([x, y])
                else:
                    continue


def fleas_distance(n, m, s, t, q, fleas):
    field = get_field(n, m, s, t, q, fleas)
    bfs_fleas(n, m, s, t, q, field)
    answer = 0
    for x, y in fleas:
        fleas_path = field[x][y]
        if fleas_path == -1:
            return -1
        answer += fleas_path
    return answer


def main():
    print(fleas_distance(*input_read()))


if __name__ == '__main__':
    main()
