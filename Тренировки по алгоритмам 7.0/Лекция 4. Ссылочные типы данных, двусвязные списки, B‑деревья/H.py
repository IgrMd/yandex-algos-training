def read_input():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a - 1, b - 1))
    requests = []
    for _ in range(k):
        cmd, a, b = input().split()
        requests.append((cmd, int(a) - 1, int(b) - 1))
    return n, m, edges, requests


def cut_graph(n: int, m: int, e: list[tuple[int, int]], requests: list[tuple[str, int, int]]):
    edges = [x for x in range(n)]
    snm: list[list] = []
    for x in edges:
        snm.append([x])
    ans = []
    for cmd, a, b in requests[::-1]:
        if cmd == 'ask':
            ans.append('YES' if edges[a] == edges[b] else 'NO')
            continue
        if edges[a] == edges[b]:
            continue
        if len(snm[edges[a]]) < len(snm[edges[b]]):
            a, b = b, a
        buf = snm[edges[b]]
        snm[edges[b]] = []
        for island in buf:
            edges[island] = edges[a]
        snm[edges[a]].extend(buf)
    return ans[::-1]


def main():
    print(*cut_graph(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
