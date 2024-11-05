import random


def read_input():
    n = int(input().strip())
    evidences = list(map(int, input().split()))
    m, k = list(map(int, input().split()))
    order = list(map(int, input().split()))
    return n, evidences, m, k, order


def slow_detective(n,
                   evidences: list,
                   m, k, order: list):
    ans = []
    for r in order:
        l = r - 1
        same_cnt = 0

        def can_move(ptr):
            if ptr == 0:
                return False
            if evidences[ptr] > evidences[ptr - 1]:
                return True
            if evidences[ptr] == evidences[ptr - 1]:
                return same_cnt < k
            return False

        while l >= 0 and can_move(l):
            if evidences[l] == evidences[l - 1]:
                same_cnt += 1
            l -= 1

        ans.append(l + 1)
    return ans


def detective(n,
              evidences: list,
              m, k, order: list):
    buf = [0] * n
    r = n - 1
    l = r
    same_cnt = 0

    def can_move(ptr):
        if ptr == 0:
            return False
        if evidences[ptr] > evidences[ptr - 1]:
            return True
        if evidences[ptr] == evidences[ptr - 1]:
            return same_cnt < k
        return False

    while r >= 0:
        if l > r:
            l = r
        while l > 0 and can_move(l):
            if evidences[l - 1] == evidences[l]:
                same_cnt += 1
            l -= 1

        buf[r] = l + 1
        if r > l and evidences[r - 1] == evidences[r]:
            same_cnt -= 1
        r -= 1

    ans = [0] * m
    for i in range(m):
        ans[i] = buf[order[i] - 1]
    return ans


def stress_test():
    while True:
        n = random.randint(1, 10)
        evidences = [random.randint(0, 100) for _ in range(n)]
        m = n
        k = random.randint(0, n)
        order = [i + 1 for i in range(m)]
        ans = detective(n, evidences, m, k, order)
        slow_ans = slow_detective(n, evidences, m, k, order)
        if ans != slow_ans:
            evidences = ' '.join(map(str, evidences))
            order = ' '.join(map(str, order))
            print(f'{n}\n{evidences}\n{m} {k}\n{order}')
            ans = ' '.join(map(str, ans))
            slow_ans = ' '.join(map(str, slow_ans))

            print(f'ans: {ans}\nslow_ans: {slow_ans}')
            break


def test():
    assert detective(6, [23, 28, 28, 33, 33, 2], 6, 0, [1, 2, 3, 4, 5, 6]) == [1, 1, 3, 3, 5, 6]
    assert detective(7, [4, 2, 3, 4, 4, 3, 3], 7, 1, [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 2, 2, 6, 6]
    assert detective(6, [3, 3, 3, 4, 4, 5], 6, 2, [1, 2, 3, 4, 5, 6]) == [1, 1, 1, 1, 2, 2]
    assert detective(7, [1, 5, 7, 2, 10, 10, 6], 7, 0, [1, 2, 3, 4, 5, 6, 7]) == [1, 1, 1, 4, 4, 6, 7]
    assert detective(5, [1, 2, 3, 4, 5], 5, 0, [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]
    assert detective(5, [5, 4, 3, 2, 1], 5, 44, [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert detective(5, [1, 1, 1, 1, 1], 5, 1, [1, 2, 3, 4, 5]) == [1, 1, 2, 3, 4]
    assert detective(1, [1], 1, 1, [1]) == [1]
    assert detective(2, [1, 2], 2, 0, [1, 2]) == [1, 1]
    assert detective(2, [2, 1], 2, 0, [1, 2]) == [1, 2]
    assert detective(1, [1], 1, 1, [1]) == [1]
    assert detective(5, [1, 1, 2, 3, 4], 5, 1, [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]
    assert detective(5, [1, 1, 1, 3, 4], 5, 1, [1, 2, 3, 4, 5]) == [1, 1, 2, 2, 2]
    assert detective(5, [1, 1, 1, 3, 4], 5, 1, [1, 2, 3, 4, 5]) == [1, 1, 2, 2, 2]
    assert detective(6, [55, 3, 3, 3, 3, 55], 6, 1, [1, 2, 3, 4, 5, 6]) == [1, 2, 2, 3, 4, 4]
    assert detective(5, [2, 2, 2, 2, 2], 5, 1, [1, 2, 3, 4, 5]) == [1, 1, 2, 3, 4]
    assert detective(5, [1, 2, 2, 2, 3], 5, 10, [1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1]
    assert detective(7, [3, 3, 1, 1, 2, 2, 4], 7, 2, [1, 2, 3, 4, 5, 6, 7]) == [1, 1, 3, 3, 3, 3, 3]

    print('tests pass')


def main():
    # test()
    # stress_test()
    # return
    print(*detective(*read_input()))


if __name__ == '__main__':
    main()
