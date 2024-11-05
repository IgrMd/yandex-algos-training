def read_input():
    n = int(input().strip())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    mood = list(map(int, input().split()))
    return n, arr_a, arr_b, mood


def algorithms(n, arr_a: list, arr_b: list, mood: list):
    a_b_i = []
    b_a_i = []
    visited = [False] * n
    ans = [0] * n
    for i in range(n):
        a_b_i.append((arr_a[i], arr_b[i], i))
        b_a_i.append((arr_b[i], arr_a[i], i))
    a_b_i.sort(key=lambda x: (-x[0], -x[1], x[2]))
    b_a_i.sort(key=lambda x: (-x[0], -x[1], x[2]))
    a, b = 0, 0
    i = 0
    while i != n:
        while visited[a_b_i[a][2]]:
            a += 1
        while visited[b_a_i[b][2]]:
            b += 1
        if mood[i] == 1:
            picked = b_a_i[b][2]
            b += 1
        else:
            picked = a_b_i[a][2]
            a += 1
        visited[picked] = True
        ans[i] = picked + 1
        i += 1

    return ans


def test():
    pass


def main():
    # test()
    print(*algorithms(*read_input()))


if __name__ == '__main__':
    main()
