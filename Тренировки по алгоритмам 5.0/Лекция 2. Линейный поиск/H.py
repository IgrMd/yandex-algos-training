def read_input():
    n, m = map(int, input().split())
    heroes = [list(map(int, input().split())) for _ in range(n)]
    return n, m, heroes


def banned_heroes(n, m, heroes: list[list]):
    max1, max1_i, max1_j = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if heroes[i][j] > max1:
                max1, max1_i, max1_j = heroes[i][j], i, j
    max2, max2_i, max2_j = 0, 0, 0
    max3, max3_i, max3_j = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if heroes[i][j] > max2 and i != max1_i:
                max2, max2_i, max2_j = heroes[i][j], i, j
            if heroes[i][j] > max3 and j != max1_j:
                max3, max3_i, max3_j = heroes[i][j], i, j
    ans_i, ans_j = max1_i, max2_j
    min_rest = max1
    for banned_i, banned_j in ((max1_i, max2_j), (max3_i, max1_j)):
        curr_max = 0
        for i in range(n):
            for j in range(m):
                if i == banned_i or j == banned_j:
                    continue
                curr_max = max(curr_max, heroes[i][j])
        if curr_max < min_rest:
            min_rest = curr_max
            ans_i, ans_j = banned_i, banned_j

    return ans_i + 1, ans_j + 1


def main():
    print(*banned_heroes(*read_input()), sep=' ')


if __name__ == '__main__':
    main()
