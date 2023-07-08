def read_input():
    m = int(input())
    n = int(input())
    return m, n


def get_sectors(m, N):
    sectors = []
    for n in range(N):
        a, b = [int(x) for x in input().split()]
        size = len(sectors)
        i = 0
        while i < size:
            ai, bi = sectors[i]
            if bi < a or b < ai:
                i += 1
                continue
            sectors[i], sectors[size - 1] = sectors[size - 1], sectors[i]
            sectors.pop()
            size -= 1
        sectors.append([a, b])
    return len(sectors)


def main():
    print(get_sectors(*read_input()))


if __name__ == '__main__':
    main()
