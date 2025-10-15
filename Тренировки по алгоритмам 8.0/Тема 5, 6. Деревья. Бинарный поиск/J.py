from heapq import heappop, heappush
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
        queue = deque()
        i = 0
        for j in range(n):
            while i < n and i - j < k + 1:
                queue.append((i, a[i]))
                i += 1
            extra = b[j]
            while extra and queue:
                it, count = queue.popleft()
                r, l = min(n - 1, it + k), max(0, it - k)
                if j > r:
                    return False
                if l > j:
                    queue.appendleft((it, count))
                    break
                if extra < count:
                    count -= extra
                    queue.appendleft((it, count))
                    extra = 0
                else:
                    extra -= count
        return False if queue else True

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
    print(interview_schedule(*read_input()))


if __name__ == '__main__':
    main()
