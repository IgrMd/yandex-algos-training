from heapq import heappop, heappush


def read_input():
    n = int(input().strip())
    d, v = [int(x) for x in input().split()]
    r = int(input().strip())
    graph = [[] for _ in range(r + 1)]
    for i in range(1, r + 1):
        a, t1, b, t2 = [int(x) for x in input().split()]
        graph[a].append((b, t1, t2))
    return n, d, v, r, graph


MAX_INT = 10 ** 9


def buses(n, d, v, r, graph):
    visited = [False] * (n + 1)
    time = [MAX_INT] * (n + 1)
    time[d] = 0
    heap = []
    heappush(heap, (0, d))
    while len(heap):
        now_time, now_stop = heappop(heap)
        if visited[now_stop]:
            continue
        visited[now_stop] = True
        for b, t1, t2 in graph[now_stop]:
            if t1 < now_time:
                continue
            if t2 < time[b]:
                time[b] = t2
                heappush(heap, (time[b], b))
    return time[v] if time[v] < MAX_INT else -1


def main():
    print(buses(*read_input()))


if __name__ == '__main__':
    main()
