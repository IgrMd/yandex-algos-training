import sys

sys.setrecursionlimit(100000)


def input_read():
    n, m = [int(x) for x in input().split()]
    graph = [list() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
    return n, m, graph


def dfs(graph, visited, now, answer):
    if visited[now] == 1:
        return False
    if visited[now] == 2:
        return True
    visited[now] = 1
    for v in graph[now]:
        if not dfs(graph, visited, v, answer):
            return False
    visited[now] = 2
    answer.append(now)
    return True


def topo_sort(n, m, graph):
    visited = [0] * (n + 1)
    answer = []
    for v in range(1, n + 1):
        if not visited[v]:
            if not dfs(graph, visited, v, answer):
                return None
    return answer[::-1]


def main():
    answer = topo_sort(*input_read())
    if answer is None:
        print(-1)
    else:
        print(*answer)


if __name__ == '__main__':
    main()
