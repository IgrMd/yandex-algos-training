def read_input():
    n = int(input())
    shirts = [int(x) for x in input().split()]
    m = int(input())
    pants = [int(x) for x in input().split()]
    return n, m, shirts, pants


def style(n, m, shirts, pants):
    l = 0
    r = 0
    wardrobe = []
    while l < n and r < m:
        if shirts[l] < pants[r]:
            wardrobe.append((shirts[l], 0))
            l += 1
        else:
            wardrobe.append((pants[r], 1))
            r += 1

    while l < n:
        wardrobe.append((shirts[l], 0))
        l += 1
    while r < m:
        wardrobe.append((pants[r], 1))
        r += 1

    max_style = wardrobe[-1][0] - wardrobe[1][0]
    pair = 0
    for i in range(len(wardrobe) - 1):
        if wardrobe[i][1] == wardrobe[i + 1][1]:
            continue
        if wardrobe[i + 1][0] - wardrobe[i][0] < max_style:
            max_style = wardrobe[i + 1][0] - wardrobe[i][0]
            pair = i
    if wardrobe[pair][1] == 0:
        return wardrobe[pair][0], wardrobe[pair + 1][0]
    else:
        return wardrobe[pair + 1][0], wardrobe[pair][0]


def main():
    print(*style(*read_input()))


if __name__ == '__main__':
    main()
