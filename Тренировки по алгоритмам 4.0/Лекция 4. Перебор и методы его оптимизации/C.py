import datetime


def read_input():
    n = int(input().strip())
    graph = [[int(x) for x in input().split()] for _ in range(n)]
    return n, graph


DIST = 0
SLICES = []


def calc_splice(n, graph, visited):
    global DIST
    global SLICES
    sum_dist = 0
    for i in range(n):
        if visited[i] == 2:
            continue
        for j in range(n):
            if visited[j] == visited[i]:
                continue
            sum_dist += graph[i][j]
    if sum_dist > DIST:
        DIST = sum_dist
        SLICES = visited.copy()


def calc_max_splice(curr_v, n, graph,
                    visited):
    if curr_v == n:
        return calc_splice(n, graph, visited)
    visited[curr_v] = 2
    calc_max_splice(curr_v + 1, n, graph, visited)
    visited[curr_v] = 1
    calc_max_splice(curr_v + 1, n, graph, visited)


def max_splice(n, graph):
    global DIST
    for i in range(n):
        for j in range(n):
            DIST = max(DIST, graph[i][j])
    visited = [0 for _ in range(n)]
    calc_max_splice(0, n, graph, visited)
    print(DIST)
    print(*SLICES)


def main():
    max_splice(*read_input())


if __name__ == '__main__':
    main()
