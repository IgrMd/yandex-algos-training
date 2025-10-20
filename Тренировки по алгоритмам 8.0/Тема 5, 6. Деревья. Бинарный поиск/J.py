import datetime
import sys


def read_input():
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b


def interview_schedule(n: int, a: list[int], b: list[int]):
    if sum(b) < sum(a):
        return -1

    left, right = 0, n
    while left < right:
        k = (left + right) // 2

        def cmp():
            i = 0
            a_extra = a[0]
            for j in range(n):
                b_extra = b[j]
                while b_extra and i - j <= k:
                    if j > i + k:
                        return False
                    if b_extra < a_extra:
                        a_extra -= b_extra
                        b_extra = 0
                    else:
                        b_extra -= a_extra
                        i += 1
                        if i == n:
                            return True
                        a_extra = a[i]
            return False

        if cmp():
            right = k
        else:
            left = k + 1
    return left


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
