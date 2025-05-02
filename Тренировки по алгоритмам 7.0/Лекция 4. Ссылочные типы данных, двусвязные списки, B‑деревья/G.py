def read_input():
    n, m = map(int, input().split())
    bridges = []
    for _ in range(m):
        a, b = map(int, input().split())
        bridges.append((a - 1, b - 1))
    return n, m, bridges


def link_islands(n: int, m: int, bridges: list[tuple[int, int]]):
    islands = [x for x in range(n)]
    snm: list[list] = []
    for x in islands:
        snm.append([x])
    for bridge in range(m):
        a, b = bridges[bridge]
        if islands[a] == islands[b]:
            continue
        if len(snm[islands[a]]) < len(snm[islands[b]]):
            a, b = b, a
        buf = snm[islands[b]]
        snm[islands[b]] = []
        for island in buf:
            islands[island] = islands[a]
        snm[islands[a]].extend(buf)
        if len(snm[islands[a]]) == n:
            return bridge + 1
    return m


def main():
    print(link_islands(*read_input()))


if __name__ == '__main__':
    main()
