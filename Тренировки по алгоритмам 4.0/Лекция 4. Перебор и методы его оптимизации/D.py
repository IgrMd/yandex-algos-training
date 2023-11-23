def read_input():
    n = int(input().strip())
    graph = [[int(x) for x in input().split()] for _ in range(n)]
    return n, graph


MAX_INT = 10 ** 9


def calc_len(curr_v, n, graph, visited):
    visited[curr_v] = True
    if sum(visited) == n:
        visited[curr_v] = False
        return graph[curr_v][0] if graph[curr_v][0] != 0 else MAX_INT
    min_len = MAX_INT
    for v in range(n):
        if graph[curr_v][v] == 0:
            continue
        if visited[v]:
            continue
        min_len = min(min_len, calc_len(v, n, graph, visited) + graph[curr_v][v])
    visited[curr_v] = False
    return min_len


def salesman_trip(n, graph):
    if n == 1:
        return 0
    visited = [False for _ in range(n)]
    distance = calc_len(0, n, graph, visited)
    return distance if distance < MAX_INT else -1


def main():
    print(salesman_trip(*read_input()))


if __name__ == '__main__':
    main()
