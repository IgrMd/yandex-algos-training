import datetime
import sys
from collections import deque


def read_input():
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b


def bin_search(left: int, right: int, cmp):
    while left < right:
        mid = (left + right) // 2
        if cmp(mid):
            right = mid
        else:
            left = mid + 1
    return left


def interview_schedule(n: int, a: list[int], b: list[int]):
    if sum(b) < sum(a):
        return -1

    def cmp(k):
        i = 0
        j = 0
        a_extra = a[i]
        while j < n and i < n:
            b_extra = b[j]
            while b_extra and i < n and i - j <= k:
                if j > i + k:
                    return False
                if b_extra < a_extra:
                    a_extra -= b_extra
                    b_extra = 0
                else:
                    b_extra -= a_extra
                    i += 1
                    if i < n:
                        a_extra = a[i]
            j += 1
        return i == n

    k = bin_search(0, n, cmp)
    return k


def test():
    def to_l(s):
        return list(map(int, s.split()))

    assert interview_schedule(4, to_l('6 14 70 1'), to_l('70 3 16 5')) == 2
    assert interview_schedule(1, to_l('2'), to_l('2')) == 0
    assert interview_schedule(1, to_l('3'), to_l('2')) == -1
    assert interview_schedule(10, to_l('6 4 9 8 6 7 4 3 6 7'), to_l('8 7 7 11 6 4 6 4 7 9')) == 1
    assert interview_schedule(6, to_l('60 27 27 27 27 27'), to_l('75 27 27 27 27 97')) == 0
    print('Tests OK')


def main():
    # test()
    # start = datetime.datetime.now()
    # sys.stdin = open('input.txt', 'r')
    print(interview_schedule(*read_input()))
    # print(datetime.datetime.now() - start)


if __name__ == '__main__':
    main()
