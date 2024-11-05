def read_input():
    n = int(input().strip())
    rooms = list(map(int, input().split()))
    return n, rooms


def openspace(n, rooms: list):
    if n == 1:
        return rooms[0]
    pref_sums = [[0, 0] for _ in range(n + 1)]
    for i in range(n):
        pref_sums[i + 1][0] = pref_sums[i][0] + rooms[i]
        pref_sums[i + 1][1] = pref_sums[i][1] + rooms[i] * i
    suff_sums = [[0, 0] for _ in range(n + 1)]
    for j in range(n - 1, -1, -1):
        suff_sums[j][0] = suff_sums[j + 1][0] + rooms[j]
        suff_sums[j][1] = suff_sums[j + 1][1] + rooms[j] * (n - j - 1)

    ans = None

    for k in range(n):
        left_part = pref_sums[k][0] * k - pref_sums[k][1]
        right_part = suff_sums[k + 1][0] * (n - k - 1) - suff_sums[k + 1][1]
        if ans is None:
            ans = left_part + right_part
        else:
            ans = min(ans, left_part + right_part)
    return ans


def test():
    assert openspace(4, [5, 2, 3, 1]) == 10
    assert openspace(5, [5, 4, 3, 2, 1]) == 15
    assert openspace(2, [5, 4]) == 4
    assert openspace(2, [5, 6]) == 5
    assert openspace(1, [5]) == 5


def main():
    # test()
    print(openspace(*read_input()))


if __name__ == '__main__':
    main()
