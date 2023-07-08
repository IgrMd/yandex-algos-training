def read_input():
    n, m = [int(x) for x in input().split()]
    ann, boris = set(), set()
    for _ in range(n):
        ann.add(int(input()))
    for _ in range(m):
        boris.add(int(input()))
    return ann, boris


def cubes(ann: set, boris: set):
    intersection = ann & boris
    ann = ann.difference(intersection)
    boris = boris.difference(intersection)
    return intersection, ann, boris


def m_print(m_set):
    print(len(m_set))
    print(*sorted(m_set))


def main():
    intersection, ann, boris = cubes(*read_input())
    m_print(intersection)
    m_print(ann)
    m_print(boris)


if __name__ == '__main__':
    main()
