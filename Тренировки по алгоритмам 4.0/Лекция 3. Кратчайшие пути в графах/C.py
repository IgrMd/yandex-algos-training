from heapq import heappop, heappush


def read_input():
    n, k = [int(x) for x in input().split()]
    graph = [[] for _ in range(n + 1)]
    for i in range(1, k + 1):
        a, b, l = [int(x) for x in input().split()]
        graph[a].append((b, l))
        graph[b].append((a, l))
    a, b = [int(x) for x in input().split()]
    return n, k, graph, a, b


MAX_INT = 10 ** 12


def best_way(n, k, graph, a, b):
    visited = [False] * (n + 1)
    dist = [MAX_INT] * (n + 1)
    dist[a] = 0
    heap = []
    heappush(heap, (0, a))
    while len(heap):
        now_dist, now = heappop(heap)
        if visited[now]:
            continue
        visited[now] = True
        for neib_i, neib_dist in graph[now]:
            if now_dist + neib_dist < dist[neib_i]:
                dist[neib_i] = now_dist + neib_dist
                heappush(heap, (dist[neib_i], neib_i))
    return dist[b] if dist[b] < MAX_INT else -1


def main():
    print(best_way(*read_input()))


if __name__ == '__main__':
    main()
