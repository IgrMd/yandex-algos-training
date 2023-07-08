from collections import deque


class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z


def input_read():
    n = int(input())
    start_x, start_y, start_z = 0, 0, 0
    cave = []
    for z in range(n):
        input()
        level = []
        for x in range(n):
            line = list(input())
            for y, c in enumerate(line):
                if c == 'S':
                    start_x, start_y, start_z = x, y, z
            level.append(line)
        cave.append(level)
    return n, start_x, start_y, start_z, cave


def bfs_cave(n, start_x, start_y, start_z, cave):
    queue = deque()
    queue.append(Point(start_x, start_y, start_z))
    cave[start_z][start_x][start_y] = 0
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while len(queue):
        now = queue.popleft()
        distance = cave[now.z][now.x][now.y] + 1
        for i in range(6):
            x = now.x + dx[i]
            y = now.y + dy[i]
            z = now.z + dz[i]
            if x < 0 or x >= n:
                continue
            if y < 0 or y >= n:
                continue
            if z < 0 or z >= n:
                continue
            if cave[z][x][y] == '.':
                cave[z][x][y] = distance
                queue.append(Point(x, y, z))
    min_path = 10 ** 6
    for line in cave[0]:
        for item in line:
            if type(item) == int:
                if item < min_path:
                    min_path = item
    return min_path


def main():
    print(bfs_cave(*input_read()))


if __name__ == '__main__':
    main()
