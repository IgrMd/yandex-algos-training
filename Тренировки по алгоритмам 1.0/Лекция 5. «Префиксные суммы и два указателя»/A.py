def read_input():
    n = int(input())
    shirts = [int(x) for x in input().split()]
    m = int(input())
    pants = [int(x) for x in input().split()]
    return n, m, shirts, pants


def style(n, m, shirts, pants):
    i = 0
    j = 0
    min_diff = float('inf')
    i_min, j_min = 0, 0
    while i < n and j < m:
        if abs(shirts[i] - pants[j]) < min_diff:
            min_diff = abs(shirts[i] - pants[j])
            i_min, j_min = i, j
        if shirts[i] < pants[j]:
            i += 1
        else:
            j += 1
    return shirts[i_min], pants[j_min]


def main():
    print(*style(*read_input()))


if __name__ == '__main__':
    main()
