import sys

sys.setrecursionlimit(100000)


def input_read():
    n = int(input())
    graph = [list() for _ in range(n + 1)]
    for i in range(1, n):
        line = [int(x) for x in input().split()]
        j = i
        while j <= n:
            if line[j - 1]:
                graph[j].append(i)
                graph[i].append(j)
            j += 1
    return n, graph


def dfs(graph, visited, now, parent, answer, status):
    if visited[now] == 1:
        status[0] = now
        return True
    if visited[now] == 2:
        return False
    visited[now] = 1
    for v in graph[now]:
        if dfs(graph, visited, v, now, answer, status):
            if v == parent:
                continue
            if not status[1]:
                answer.append(now)
            if status[0] == now:
                status[1] = True
            return True
    visited[now] = 2
    return False


def cycle(n, graph):
    visited = [0] * (n + 1)
    answer = []
    status = [0, False]
    for v in range(1, n + 1):
        if not visited[v]:
            if dfs(graph, visited, v, v, answer, status):
                break
    return answer


def main():
    answer = cycle(*input_read())
    if not len(answer):
        print('NO')
    else:
        print('YES')
        print(len(answer))
        print(*answer)


if __name__ == '__main__':
    main()
