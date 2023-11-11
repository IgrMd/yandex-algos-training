def read_input():
    n, s, f = [int(x) for x in input().split()]
    graph = [[-1] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i].extend([int(x) for x in input().split()])
    return n, s, f, graph


MAX_INT = 10 ** 6


def find_best_unvisited(visited, dist, n):
    min_dist = MAX_INT
    index = None
    for i in range(1, n + 1):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            index = i
    return index


def best_way(n, s, f, graph):
    visited = [False] * (n + 1)
    dist = [MAX_INT] * (n + 1)
    dist[s] = 0
    while now := find_best_unvisited(visited, dist, n):
        visited[now] = True
        now_dst = dist[now]
        for neib_i in range(1, n + 1):
            if graph[now][neib_i] <= 0:
                continue
            dist[neib_i] = min(dist[neib_i], now_dst + graph[now][neib_i])
    return dist[f] if dist[f] < MAX_INT else -1


def main():
    print(best_way(*read_input()))


if __name__ == '__main__':
    main()
