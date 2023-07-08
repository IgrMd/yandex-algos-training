def input_read():
    n, m = [int(x) for x in input().split()]
    graph = [list() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = [int(x) for x in input().split()]
        graph[v1].append(v2)
        graph[v2].append(v1)
    return n, m, graph


def dfs(graph, visited, now):
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v)


def component(n, m, graph):
    visited = [False] * (n + 1)
    dfs(graph, visited, 1)
    answer = []
    for i, v in enumerate(visited):
        if v:
            answer.append(i)
    answer.sort()
    return len(answer), answer


def main():
    count, answer = component(*input_read())
    print(count)
    print(*answer)


if __name__ == '__main__':
    main()
