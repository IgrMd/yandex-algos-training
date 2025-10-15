import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def read_input():
    n = int(input().strip())
    persons = list(map(int, input().split()))
    graph = [list() for _ in range(n)]
    for _ in range(n - 1):
        v, u = map(int, input().split())
        v, u = v - 1, u - 1
        graph[v].append(u)
        graph[u].append(v)
    return n, persons, graph


def pickup_point(n: int, persons: list[int], graph: list[list[int]]):
    if n == 1:
        return 1
    queues = [defaultdict(int) for a in graph]

    def travers_first(curr: int, parent: int):
        sum_queue = persons[curr]
        for adj in graph[curr]:
            if adj == parent:
                continue
            queue = travers_first(adj, curr)
            queues[curr][adj] = queue
            sum_queue += queue
        return sum_queue

    travers_first(0, -1)

    def traverse_second(curr: int, parent: int, queue_from_parent: int):
        if parent in graph[curr]:
            queues[curr][parent] = queue_from_parent
        sum_queue = sum(queues[curr].values()) + persons[curr]
        for adj in graph[curr]:
            if adj == parent:
                continue
            traverse_second(adj, curr, sum_queue - queues[curr][adj])

    traverse_second(0, -1, 0)

    ans = float('inf')
    ans_i = -1
    for i in range(n):
        cur_max = max(persons[i], max(queues[i].values()))
        if cur_max < ans:
            ans_i = i + 1
            ans = cur_max
    return ans_i


def main():
    print(pickup_point(*read_input()))


if __name__ == '__main__':
    # test()
    main()
