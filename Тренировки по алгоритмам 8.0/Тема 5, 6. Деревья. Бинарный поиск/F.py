from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


def successor():
    n = int(input().strip())
    graf = defaultdict(lambda: list())
    root = 0
    for i, acc in enumerate(map(int, input().split())):
        if acc == 0:
            root = i + 1
            continue
        graf[acc].append(i + 1)
    m = int(input().strip())
    reqs = defaultdict(lambda: list())
    for i in range(m):
        a, b = map(int, input().split())
        reqs[b].append((a, i))

    ans = []
    curr_ancestors = set()

    def iterate(b):
        if b in reqs:
            for a, i in reqs[b]:
                ans.append((i, int(a in curr_ancestors)))
        curr_ancestors.add(b)
        for adj in graf[b]:
            iterate(adj)
        curr_ancestors.remove(b)

    iterate(root)

    ans.sort()

    print('\n'.join(map(lambda x: str(x[1]), ans)))


if __name__ == '__main__':
    successor()
