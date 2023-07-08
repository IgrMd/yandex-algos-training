import sys

sys.setrecursionlimit(100000)


def read_input():
    n, m = [int(x) for x in input().split()]
    field = [[int(x) for x in input().split()] for _ in range(n)]
    graph = [[] for _ in range(n * m)]
    i_neibs = [0, -1, 0, 1]
    j_neibs = [-1, 0, 1, 0]
    vertexes_to_height = []
    for i in range(n):
        for j in range(m):
            v = i + j * n
            this = field[i][j]
            vertexes_to_height.append([v, this])
            for k in range(4):
                i_neib = i + i_neibs[k]
                j_neib = j + j_neibs[k]
                if i_neib < 0 or i_neib >= n:
                    continue
                if j_neib < 0 or j_neib >= m:
                    continue
                v_neib = i_neib + j_neib * n
                neib = field[i_neib][j_neib]
                if this <= neib:
                    graph[v].append(v_neib)
    vertexes_to_height.sort(key=lambda x: x[1])
    return n, m, graph, vertexes_to_height


def dfs(graph, visited, now, component):
    if visited[now] == component:
        return
    visited[now] = component
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v, component)


def traps(n, m, graph: list, vertexes_to_height: list):
    visited = [0] * n * m
    for comp, vertex_to_height in enumerate(vertexes_to_height, 1):
        v = vertex_to_height[0]
        if not visited[v]:
            dfs(graph, visited, v, comp)
            comp += 1
    answer = set(visited)
    return len(answer)


def main():
    print(traps(*read_input()))


if __name__ == '__main__':
    main()
