def multigraph():
    n, m = map(int, input().split())
    edges = set()
    for _ in range(m):
        a, b = map(int, input().split())
        if a == b:
            continue
        if (a, b) in edges or (b, a) in edges:
            continue
        edges.add((a, b))
    print(n, len(edges))
    for a, b in edges:
        print(a, b)


def main():
    multigraph()


if __name__ == '__main__':
    main()
