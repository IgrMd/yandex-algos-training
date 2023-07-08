from collections import defaultdict


class StopPair:
    def __init__(self, s1, s2):
        self.s1 = min(s1, s2)
        self.s2 = max(s1, s2)

    def __eq__(self, other):
        return self.s1 == other.s1 and self.s2 == other.s2

    def __hash__(self):
        return self.s1 * 63 + self.s2 * 63 * 63


def input_read():
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    stop_to_line = defaultdict(list)
    weights = dict()
    for k in range(m):
        line = [int(x) for x in input().split()]
        for i in range(2, len(line)):
            v1, v2 = line[i] + k * n, line[i - 1] + k * n
            graph[v1].append(v2)
            graph[v2].append(v1)
            weights[StopPair(v1, v2)] = 0
        for i in range(1, len(line)):
            v = line[i]
            if v in stop_to_line:
                for line_n in stop_to_line[v]:
                    v1 = v + k * n
                    v2 = v + line_n * n
                    graph[v1].append(v2)
                    graph[v2].append(v1)
                    weights[StopPair(v1, v2)] = 1

            stop_to_line[v].append(k)
    start, end = [int(x) for x in input().split()]
    return n, m, start, end, graph, stop_to_line, weights


MAX_PATH = 10 ** 5


def bfs_metro(n, m, start_v, graph, weights):
    distances = [[] for _ in range(n * m + 1)]
    distances[0].append(start_v)
    visited = [MAX_PATH] * (n * m + 1)
    visited[start_v] = 0
    for i in range(len(distances)):
        if not len(distances[i]):
            continue
        j = 0
        while j < len(distances[i]):
            v_now = distances[i][j]
            for v in graph[v_now]:
                weight = weights[StopPair(v_now, v)]
                if visited[v] <= i + weight:
                    continue
                distances[i + weight].append(v)
                visited[v] = i + weight
            j += 1
    return visited


def transfers(n, m, start, end, graph, stop_to_line, weights):
    min_path = MAX_PATH
    for start_line in stop_to_line[start]:
        start_v = start_line * n + start
        visited = bfs_metro(n, m, start_v, graph, weights)
        for end_line in stop_to_line[end]:
            end_v = end_line * n + end
            end_path = visited[end_v]
            if end_path < min_path:
                min_path = end_path
    return min_path if min_path != MAX_PATH else -1


def main():
    print(transfers(*input_read()))


if __name__ == '__main__':
    main()
