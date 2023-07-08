char_to_x = {}
x_to_char = {}

for i, c in enumerate('abcdefgh', 1):
    char_to_x[c] = i
    x_to_char[i] = c


def read_input():
    horse1, horse2 = input().split()
    horse1_x, horse1_y = char_to_x[horse1[0]], int(horse1[1])
    horse2_x, horse2_y = char_to_x[horse2[0]], int(horse2[1])
    return horse1_x, horse1_y, horse2_x, horse2_y


def bfs(horse1_x, horse1_y, horse2_x, horse2_y):
    n = 8
    N = n + 1
    distances1 = [[[horse1_x, horse1_y]]]
    distances2 = [[[horse2_x, horse2_y]]]
    field = [[[0, 0] for _ in range(N)] for _ in range(9)]
    field[horse1_x][horse1_y][0] = 1
    field[horse2_x][horse2_y][0] = 2

    distance1, distance2 = 0, 0
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    while distance1 < len(distances1) and distance2 < len(distances2):
        for now_x1, now_y1 in distances1[distance1]:
            distance1 = field[now_x1][now_y1][1] + 1
            for k in range(len(dx)):
                x = now_x1 + dx[k]
                y = now_y1 + dy[k]
                if x < 1 or x >= N:
                    continue
                if y < 1 or y >= N:
                    continue
                if field[x][y][0] == 2:
                    return -1
                if field[x][y][1] < distance1:
                    field[x][y][0] = 1
                    field[x][y][1] = distance1
                    if distance1 >= len(distances1):
                        distances1.append([])
                    distances1[distance1].append([x, y])
        for now_x2, now_y2 in distances2[distance2]:
            distance2 = field[now_x2][now_y2][1] + 1
            for k in range(len(dx)):
                x = now_x2 + dx[k]
                y = now_y2 + dy[k]
                if x < 1 or x >= N:
                    continue
                if y < 1 or y >= N:
                    continue
                if field[x][y][0] == 1:
                    return distance2
                if field[x][y][1] < distance2:
                    field[x][y][0] = 2
                    field[x][y][1] = distance2
                    if distance1 >= len(distances2):
                        distances2.append([])
                    distances2[distance2].append([x, y])
    return -1


def traps(n, m, graph: list, vertexes_to_height: list):
    visited = [0] * n * m
    for comp, vertex_to_height in enumerate(vertexes_to_height, 1):
        v = vertex_to_height[0]
        if not visited[v]:
            bfs(graph, visited, v, comp)
            comp += 1
    answer = set(visited)
    return len(answer)


def main():
    print(bfs(*read_input()))


if __name__ == '__main__':
    main()
