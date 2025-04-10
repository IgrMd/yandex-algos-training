def read_input():
    n, m = map(int, input().split())
    groups = list(map(int, input().split()))
    rooms = list(map(int, input().split()))
    groups = [(groups[i], i) for i in range(n)]
    rooms = [(rooms[i], i) for i in range(m)]
    return n, m, groups, rooms


def computer_for_everyone(n: int, m: int, groups: list[tuple[int, int]], rooms: list[tuple[int, int]]):
    ans = [0] * n
    groups.sort(key=lambda x: x[0])
    rooms.sort(key=lambda x: x[0])
    j = 0
    res = 0
    for group_count, group_id in groups:
        while j < m and rooms[j][0] <= group_count:
            j += 1
        if j < m:
            ans[group_id] = rooms[j][1] + 1
            res += 1
            j += 1
    return res, ans


def main():
    num, nums = computer_for_everyone(*read_input())
    print(num)
    print(*nums)


if __name__ == '__main__':
    main()
