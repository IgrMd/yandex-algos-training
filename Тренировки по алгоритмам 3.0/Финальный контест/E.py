from collections import deque, defaultdict

H, W = [int(x) for x in input().split()]
INF = 10 ** 6


class Point:
    def __init__(self, x: int, y: int, d: int):
        self.x, self.y, self.d = x, y, d

    def __eq__(self, other):
        return (self.x, self.y, self.d) == (other.x, other.y, other.d)

    def __hash__(self):
        return self.x * 63 + self.y * 63 * 63 + self.d * 63 * 63 * 63

    def to_vertex(self):
        return self.y + self.x * H + self.d * H * W

    def __str__(self):
        return f'<{self.x},{self.y},{self.d}>'


def read_input():
    field = ['X' * (W + 1)]
    for _ in range(H):
        field.append(input() + 'X')
    field.reverse()
    start = [int(x) - 1 for x in input().split()]
    start = Point(start[0], start[1], 8)
    end = [int(x) - 1 for x in input().split()]
    end = Point(end[0], end[1], 8)
    return H, W, field, start, end


def leonide(H, W, field, start: Point, end: Point):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
    visited = [INF] * (H * W * 9)
    visited[start.to_vertex()] = 1
    queue = deque()
    queue.append(start)
    while len(queue):
        now = queue.popleft()
        if now.d == 8:
            for i in range(8):
                x = now.x + dx[i]
                y = now.y + dy[i]
                if field[y][x] != '.':
                    continue
                v = Point(x, y, i)
                cur_dst = visited[now.to_vertex()]
                if cur_dst < visited[v.to_vertex()]:
                    visited[v.to_vertex()] = cur_dst
                    queue.appendleft(v)
        else:
            v = Point(now.x, now.y, 8)
            cost = 1
            cur_dst = visited[now.to_vertex()] + cost
            if cur_dst < visited[v.to_vertex()]:
                visited[v.to_vertex()] = cur_dst
                queue.append(v)

            x = now.x + dx[now.d]
            y = now.y + dy[now.d]
            if field[y][x] != '.':
                continue
            v = Point(x, y, now.d)
            cur_dst = visited[now.to_vertex()]
            if cur_dst < visited[v.to_vertex()]:
                visited[v.to_vertex()] = cur_dst
                queue.appendleft(v)

    turns = INF
    for i in range(8):
        if visited[Point(end.x, end.y, i).to_vertex()] < turns:
            turns = visited[Point(end.x, end.y, i).to_vertex()]
    return turns if turns != INF else -1


def main():
    print(leonide(*read_input()))


if __name__ == '__main__':
    main()
