from heapq import heappop, heappush

MAX_INT = 10 ** 12
MAX_TIME = 24 * 60
TRUCK_WEIGHT = 3 * (10 ** 6)


def read_input():
    n, m = [int(x) for x in input().split()]
    graph = [[] for _ in range(n + 1)]
    max_road_weight = 0
    for _ in range(m):
        a, b, t, w = [int(x) for x in input().split()]
        graph[a].append((b, t, w))
        graph[b].append((a, t, w))
        max_road_weight = max(max_road_weight, w)
    return n, m, graph, max_road_weight


def bin_search(left: int, right: int, check, params):
    while left < right:
        mid = (left + right) // 2
        if check(mid, *params):
            left = mid + 1
        else:
            right = mid
    if not check(left, *params):
        left -= 1
    return left


def check_weight(max_road_weight, n, graph):
    visited = [False] * (n + 1)
    time = [MAX_INT] * (n + 1)
    time[1] = 0
    heap = []
    heappush(heap, (0, 1))
    while len(heap):
        now_time, now = heappop(heap)
        if visited[now]:
            continue
        visited[now] = True
        for next_road, next_road_time, next_road_weight in graph[now]:
            if next_road_weight < max_road_weight:
                continue
            if now_time + next_road_time < time[next_road]:
                time[next_road] = now_time + next_road_time
                heappush(heap, (time[next_road], next_road))
    return time[n] <= MAX_TIME


def best_way(n, m, graph, max_road_weight):
    if n == 1:
        return 10 ** 7
    weight = bin_search(TRUCK_WEIGHT, max_road_weight, check_weight, (n, graph))
    if weight < TRUCK_WEIGHT:
        return 0
    return (weight - TRUCK_WEIGHT) // 100


def main():
    print(best_way(*read_input()))


if __name__ == '__main__':
    main()
