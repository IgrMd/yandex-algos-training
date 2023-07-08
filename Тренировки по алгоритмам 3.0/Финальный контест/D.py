import sys

sys.setrecursionlimit(100000)


class Point:
    def __init__(self, coordinates: str = None, x=None, y=None):
        if coordinates is None:
            self.x, self.y = x, y
        else:
            self.x, self.y = [int(x) for x in coordinates.split()]

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return self.x * 63 + self.y * 63 * 63


def read_input():
    xl, xr = [int(x) for x in input().split()]
    r = int(input())
    n = int(input())

    points = [Point(input()) for _ in range(n)]

    return xl, xr, r, n, points


def dfs(graph, visited, now):
    if visited[now]:
        return
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v)


def distance(point1: Point, point2: Point):
    return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2


def check(graph, points_l, points_r):
    visited = [False] * len(graph)
    for v in points_l:
        if not visited[v]:
            dfs(graph, visited, v)
    for v in points_r:
        if visited[v]:
            return False
    return True


def form_graph(points, max_dst):
    graph = [[] for _ in range(len(points))]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) < max_dst:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def bin_search(points, distances, begin, end, points_l, points_r):
    mid = (begin + end) // 2
    dist_mid = distances[mid]
    graph = form_graph(points, dist_mid)
    checked = check(graph, points_l, points_r)
    if checked:
        if mid == len(distances) - 1:
            return dist_mid
        graph = form_graph(points, distances[mid + 1])
        checked2 = check(graph, points_l, points_r)
        if not checked2:
            return dist_mid
    if checked:
        begin = mid + 1
    else:
        end = mid
    return bin_search(points, distances, begin, end, points_l, points_r)


def bed(xl, xr, r, n, points):
    distances = set()
    points_l = set()
    points_r = set()

    for i in range(n):
        for j in range(i + 1, n):
            distances.add(distance(points[i], points[j]))
        point_l = Point(None, xl - r, points[i].y)
        point_r = Point(None, xr + r, points[i].y)
        points.append(point_l)
        points.append(point_r)
        distances.add(distance(points[i], point_l))
        distances.add(distance(points[i], point_r))
        points_l.add(point_l)
        points_r.add(point_r)
    points = list(set(points))
    points_l = [i for i in range(len(points)) if points[i] in points_l]
    points_r = [i for i in range(len(points)) if points[i] in points_r]

    distances = sorted(distances)
    return bin_search(points, distances, 0, len(distances), points_l, points_r) ** 0.5 - 2 * r


def main():
    max_bed = bed(*read_input())
    if max_bed <= 0:
        print(0)
    else:
        print(f'{max_bed:.4f}')


if __name__ == '__main__':
    main()
