import sys

sys.setrecursionlimit(100000)


def read_input():
    n, m = [int(x) for x in input().split()]
    graph = [list() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v2].append(v1)
    return n, m, graph


def dfs(graph, visited, now):
    visited[now] = 1
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v)


def first_vertex(n, m, graph):
    visited = [0] * (n + 1)
    dfs(graph, visited, 1)
    answer = [i for i in range(n + 1) if visited[i]]
    answer.sort()
    return answer


def main():
    print(*first_vertex(*read_input()))


if __name__ == '__main__':
    main()
