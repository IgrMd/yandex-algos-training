def read_input():
    l, k = [int(x) for x in input().split()]
    bench = [0] * l
    legs = [int(x) for x in input().split()]
    for leg in legs:
        bench[leg] = 1
    return l, k, bench


def legs_needed(l: int, k: int, bench: list[int]):
    if l % 2 == 1 and bench[l // 2] == 1:
        return [l // 2]
    i = (l - 1) // 2
    j = l // 2
    while i > 0 and bench[i] != 1:
        i -= 1
    while j < l and bench[j] != 1:
        j += 1
    return i, j


def main():
    print(*legs_needed(*read_input()))


if __name__ == '__main__':
    main()
