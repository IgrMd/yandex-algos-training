from collections import deque


def input_read():
    n = int(input())
    input_list = [[int(x) for x in input().split()] for _ in range(n)]
    graph = [list() for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n):
            if input_list[i][j]:
                graph[i + 1].append(j + 1)
                graph[j + 1].append(i + 1)
    start, end = [int(x) for x in input().split()]
    return n, graph, start, end


def bfs(n, graph, start, end):
    distances = [-1] * (n + 1)
    parents = [-1] * (n + 1)
    queue = deque()
    queue.append(start)
    distances[start] = 0
    while len(queue):
        now = queue.popleft()
        distance = distances[now] + 1
        for v in graph[now]:
            if distances[v] != -1:
                continue
            distances[v] = distance
            parents[v] = now
            queue.append(v)
    answer = [end]
    prev = parents[end]
    while prev != -1:
        answer.append(prev)
        prev = parents[prev]

    return distances[end], answer[::-1]


def main():
    length, path = bfs(*input_read())
    print(length)
    if length > 0:
        print(*path)


if __name__ == '__main__':
    main()
