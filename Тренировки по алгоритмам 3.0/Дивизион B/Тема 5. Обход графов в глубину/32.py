from collections import defaultdict
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


def dfs(graph, visited, now, comp_num):
    if visited[now]:
        return
    visited[now] = comp_num
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v, comp_num)


def components(n, m, graph):
    visited = [0] * (n + 1)
    comp_num = 0
    for v in range(1, n + 1):
        comp_num += 1
        dfs(graph, visited, v, comp_num)
    answer = defaultdict(list)
    for i in range(1, n + 1):
        answer[visited[i]].append(i)
    return answer


def main():
    answer = components(*input_read())
    print(len(answer))
    for component in answer.values():
        print(len(component))
        print(*component)


if __name__ == '__main__':
    main()
