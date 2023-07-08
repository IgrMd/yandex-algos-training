from collections import deque


def dfs(graph, visited, now, comp_num):
    if visited[now]:
        return
    visited[now] = comp_num
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v, comp_num)


def assign_components(graph, sub_graph, n):
    visited = [0] * (n + 1)
    comp_num = len(graph)
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(sub_graph, visited, v, comp_num)
            comp_num += 1
    for v in range(1, n + 1):
        comp_num = visited[v]
        if comp_num >= len(graph):
            graph.append([])
        graph[comp_num].append(v)
        graph[v].append(comp_num)


def read_input():
    n, k = [int(x) for x in input().split()]
    graph = [[] for _ in range(n + 1)]
    for card in range(k):
        r = int(input())
        sub_graph = [[] for _ in range(n + 1)]
        for __ in range(r):
            v1, v2 = [int(x) for x in input().split()]
            sub_graph[v1].append(v2)
            sub_graph[v2].append(v1)
        assign_components(graph, sub_graph, n)
    return n, k, graph


def bfs(n, k, graph):
    inf = 10 ** 7
    visited = [inf for _ in range(len(graph))]
    visited[1] = 0
    queue = deque()
    queue.append(1)
    while len(queue):
        now = queue.popleft()
        for v in graph[now]:
            cur_distance = visited[now] + (1 if now > v else 0)
            if cur_distance < visited[v]:
                visited[v] = cur_distance
                queue.append(v)
    return visited[n] if visited[n] != inf else -1


def main():
    print(bfs(*read_input()))


if __name__ == '__main__':
    main()
