import sys

sys.setrecursionlimit(100000)


class Point:
    def __init__(self, coordinates: str = None):
        if coordinates is None:
            self.x, self.y = -1, -1
        else:
            self.x, self.y = [int(x) for x in coordinates.split()]


def read_input():
    n = int(input())
    points = [Point(input()) for _ in range(n)]
    return n, points


def dfs(graph, visited, now, color):
    if visited[now] == 3 - color:
        return False
    if visited[now] == color:
        return True
    visited[now] = color
    for v in graph[now]:
        if not dfs(graph, visited, v, 3 - color):
            return False
    return True


def distance(point1: Point, point2: Point):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


def check(n, graph):
    visited = [0] * n
    for v in range(n):
        if not visited[v]:
            if not dfs(graph, visited, v, 1):
                return False, visited
    return True, visited


def form_graph(n, points, max_dst):
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if distance(points[i], points[j]) < max_dst - 1e-10:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def bin_search(n, points, distances, begin, end):
    mid = (begin + end) // 2
    dist_mid = distances[mid]
    graph = form_graph(n, points, dist_mid)
    checked, answer = check(n, graph)
    if checked:
        if mid == len(distances) - 1:
            return dist_mid / 2, answer
        graph = form_graph(n, points, distances[mid + 1])
        checked2, answer2 = check(n, graph)
        if not checked2:
            return dist_mid / 2, answer
    if checked:
        begin = mid + 1
    else:
        end = mid
    return bin_search(n, points, distances, begin, end)


def power(n, points):
    distances = set()
    for i in range(n):
        for j in range(i + 1, n):
            distances.add(distance(points[i], points[j]))
    distances = sorted(distances)
    return bin_search(n, points, distances, 0, len(distances))


def main():
    max_power, answer = power(*read_input())
    print(f'{max_power:.9f}')
    print(*answer)


if __name__ == '__main__':
    main()
