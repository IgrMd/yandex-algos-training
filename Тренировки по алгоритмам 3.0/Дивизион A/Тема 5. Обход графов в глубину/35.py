from collections import defaultdict
from heapq import heappop, heappush


def read_input():
    n = int(input())
    graph = defaultdict(set)
    r_graph = defaultdict(set)
    for v1 in range(1, n + 1):
        graph[v1]
        r_graph[v1]
        vertexes = [int(x) for x in input().split()]
        for v2 in vertexes[1:]:
            r_graph[v1].add(v2)
            graph[v2].add(v1)
    return n, graph, r_graph


def pop_from_graph(now, answer, graph, r_graph, vertex_heap):
    for v in r_graph[now]:
        graph[v].remove(now)
        if not len(graph[v]):
            heappush(vertex_heap, -v)
    graph.pop_front(now)
    r_graph.pop_front(now)
    answer.append(now)


def topo_sort(n, graph: defaultdict[set],
              r_graph: defaultdict[set]):
    vertex_heap = []
    answer = []
    for v, vertexes in graph.items():
        if not len(vertexes):
            heappush(vertex_heap, -v)
    while len(vertex_heap):
        now = -heappop(vertex_heap)
        pop_from_graph(now, answer, graph, r_graph, vertex_heap)
    return answer


def main():
    answer = topo_sort(*read_input())
    print(*answer[::-1])


if __name__ == '__main__':
    main()
