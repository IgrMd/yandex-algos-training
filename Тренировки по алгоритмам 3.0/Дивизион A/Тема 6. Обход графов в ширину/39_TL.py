from collections import deque


def read_input():
    n, k = [int(x) for x in input().split()]
    graph = [list() for _ in range(n + 1)]
    edges = []
    for edge_num in range(k):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
        graph[v2].append(v1)
        edges.append((v1, v2))
    m = int(input())
    robots = [int(x) for x in set(input().split())]
    m = len(robots)
    return n, k, m, graph, robots, edges


def dfs(now, graph, visited):
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            dfs(v, graph, visited)


def check(n, k, graph, robots):
    visited = [False for _ in range(n + 1)]
    dfs(robots[0], graph, visited)
    for v in robots:
        if not visited[v]:
            return False
    return True


def bfs(graph, visited, start):
    queue = deque()
    queue.append((start, 0))
    visited[start][0] = 0
    while len(queue):
        now, dst = queue.popleft()
        distance = dst + 1
        parity = distance % 2
        for v in graph[now]:
            if distance < visited[v][parity]:
                visited[v][parity] = distance
                queue.append((v, distance))


def min_path(n, k, m, graph, robots, edges):
    infinite = 10 ** 6
    if m == 1:
        return 0
    if not check(n, k, graph, robots):
        return -1
    visited = [[[infinite, infinite] for _ in range(n + 1)] for _ in range(m)]
    for i in range(m):
        bfs(graph, visited[i], robots[i])
    max_path = infinite
    for room_i in range(1, n + 1):
        max_even_path = max({visited[x][room_i][0] for x in range(m)})
        max_odd_path = max({visited[x][room_i][1] for x in range(m)})
        max_path = min(max_path, max_even_path, max_odd_path)

    for v1, v2 in edges:
        max_edge_even = max({min(visited[x][v1][0], visited[x][v2][0]) for x in range(m)})
        max_edge_odd = max({min(visited[x][v1][1], visited[x][v2][1]) for x in range(m)})
        max_path = min(max_path, min(max_edge_even, max_edge_odd) + 0.5)
    return max_path


def main():
    print(min_path(*read_input()))


if __name__ == '__main__':
    main()
