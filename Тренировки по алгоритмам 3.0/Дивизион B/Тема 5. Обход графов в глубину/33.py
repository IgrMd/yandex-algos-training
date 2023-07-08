import sys

sys.setrecursionlimit(100000)


def input_read():
    n, m = [int(x) for x in input().split()]
    graph = [list() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
        graph[v2].append(v1)
    return n, m, graph


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


def two_groups(n, m, graph):
    visited = [0] * (n + 1)
    for v in range(1, n + 1):
        if not visited[v]:
            if not dfs(graph, visited, v, 1):
                return False
    return True


def main():
    if two_groups(*input_read()):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
