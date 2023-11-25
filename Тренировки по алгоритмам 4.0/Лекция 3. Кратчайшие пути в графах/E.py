import math
import sys

sys.setrecursionlimit(100000)


def read_input():
    n = int(input().strip())
    towns = [0]
    for _ in range(n):
        t, v = [int(x) for x in input().split()]
        towns.append((t, v))
    roads = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, s = [int(x) for x in input().split()]
        roads[a].append((b, s))
        roads[b].append((a, s))
    return n, towns, roads


def dfs(curr_dist, curr_town, distances, roads):
    if distances[curr_town] != -1:
        return
    distances[curr_town] = curr_dist
    for next_town, dist in roads[curr_town]:
        dfs(curr_dist + dist, next_town, distances, roads)


def calc_dist_matrix(n, roads: list) -> list[list]:
    dist_matrix = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for curr_town in range(1, n + 1):
        distances = dist_matrix[curr_town]
        distances[curr_town] = 0
        for next_town, dist in roads[curr_town]:
            dfs(dist, next_town, distances, roads)
    return dist_matrix


def calc_time_matrix(n, towns: list, dist_matrix: list[list]) -> list[list]:
    for from_town in range(1, n + 1):
        for to_town in range(1, n + 1):
            if from_town == to_town:
                dist_matrix[from_town][to_town] = 0
                continue
            t, v = towns[to_town]
            dist_matrix[from_town][to_town] = dist_matrix[from_town][to_town] / v + t
    return dist_matrix


def find_best_unvisited(visited, time, n):
    min_time = math.inf
    index = None
    for i in range(1, n + 1):
        if not visited[i] and time[i] < min_time:
            min_time = time[i]
            index = i
    return index


def time_to_reach_moscow(n, towns, roads):
    matrix = calc_dist_matrix(n, roads)
    matrix = calc_time_matrix(n, towns, matrix)
    visited = [False] * (n + 1)
    times = [math.inf] * (n + 1)
    parent = [-1] * (n + 1)
    times[1] = 0
    while now := find_best_unvisited(visited, times, n):
        visited[now] = True
        now_time = times[now]
        for neib_i in range(1, n + 1):
            if matrix[now][neib_i] <= 0:
                continue
            if times[neib_i] > now_time + matrix[now][neib_i]:
                times[neib_i] = now_time + matrix[now][neib_i]
                parent[neib_i] = now

    max_town, max_time = 0, 0
    for i in range(1, n + 1):
        if max_time < times[i]:
            max_time = times[i]
            max_town = i
    way = []
    now_town = max_town
    while now_town != 1:
        way.append(now_town)
        now_town = parent[now_town]
    way.append(1)
    print(max_time)
    print(*way)


def main():
    time_to_reach_moscow(*read_input())


if __name__ == '__main__':
    main()
