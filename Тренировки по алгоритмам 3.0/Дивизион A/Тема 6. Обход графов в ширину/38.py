from collections import deque, defaultdict


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __hash__(self):
        return self.x * 63 + self.y * 63 * 63

    def __str__(self):
        return f'{self.x},{self.y}'


def read_input():
    n, m = [int(x) for x in input().split()]
    max_actions = n * m
    field = []
    holes = []
    for i in range(n):
        field.append([int(x) for x in input().split()])
        for j, char in enumerate(field[i]):
            if char == 0:
                field[i][j] = max_actions
                continue
            elif char == 1:
                field[i][j] = '*'
            elif char == 2:
                holes.append([i, j])
                field[i][j] = max_actions
    return n, m, field, holes


def get_neighbours(n, m, field: list[list], now: Point):
    neighbours = list()
    y = now.y
    while y + 1 < m and field[now.x][y + 1] != '*':
        y += 1
    if y != now.y:
        neighbours.append(Point(now.x, y))

    y = now.y
    while y - 1 >= 0 and field[now.x][y - 1] != '*':
        y -= 1
    if y != now.y:
        neighbours.append(Point(now.x, y))

    x = now.x
    while x + 1 < n and field[x + 1][now.y] != '*':
        x += 1
    if x != now.x:
        neighbours.append(Point(x, now.y))

    x = now.x
    while x - 1 >= 0 and field[x - 1][now.y] != '*':
        x -= 1
    if x != now.x:
        neighbours.append(Point(x, now.y))

    return neighbours


def assign_points(now: Point, neighbour: Point, graph: defaultdict[Point, set]):
    graph[now].add(neighbour)
    if now.y == neighbour.y:
        for x in range(min(now.x, neighbour.x) + 1, max(now.x, neighbour.x)):
            graph[now].add(Point(x, now.y))
    if now.x == neighbour.x:
        for y in range(min(now.y, neighbour.y) + 1, max(now.y, neighbour.y)):
            graph[now].add(Point(now.x, y))


def get_graph(n, m, field) -> (defaultdict[Point, set], dict, set):
    point_to_neighbours = dict()
    graph = defaultdict(set)
    point_queue = deque()
    point_queue.append(Point(0, 0))
    while len(point_queue):
        now = point_queue.popleft()
        if now in graph:
            continue
        neighbours = get_neighbours(n, m, field, now)
        point_to_neighbours[now] = neighbours.copy()
        for neighbour in neighbours:
            assign_points(now, neighbour, graph)
            point_queue.append(neighbour)

    return graph, point_to_neighbours


def bfs(n, m, field, holes):
    graph, point_to_neighbours = get_graph(n, m, field)
    field[0][0] = 0
    start = Point(0, 0)
    distances = [[start]]
    distance = 0
    while distance < len(distances):
        for now in distances[distance]:
            distance = field[now.x][now.y] + 1
            for point in graph[now]:
                if distance < field[point.x][point.y]:
                    field[point.x][point.y] = distance
                    if distance >= len(distances):
                        distances.append([])
                    if point in point_to_neighbours[now]:
                        distances[distance].append(point)

    max_actions = n * m
    for hole_x, hole_y in holes:
        if field[hole_x][hole_y] < max_actions:
            max_actions = field[hole_x][hole_y]
    return max_actions


def main():
    print(bfs(*read_input()))


if __name__ == '__main__':
    main()
