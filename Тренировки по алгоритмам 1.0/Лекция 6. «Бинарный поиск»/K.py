def read_input():
    n, l = [int(x) for x in input().split()]
    sequences = [get_seq([int(x) for x in input().split()], l) for _ in range(n)]
    return n, l, sequences


def get_seq(data, l):
    x1, d, a, c, m = data
    x = [x1]
    for i in range(l - 1):
        x.append(x[-1] + d)
        d = (a * d + c) % m
    return x


def lower_bound(left: int, right: int, arr, value):
    right -= 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid
    if arr[left] < value:
        left += 1
    return left


def upper_bound(left: int, right: int, arr, value):
    right -= 1
    while left < right:
        mid = (left + right + 1) // 2
        if value < arr[mid]:
            right = mid - 1
        else:
            left = mid
    if not value < arr[left]:
        left += 1
    return left


def test_lower_bound():
    arr = [2, 4, 6, 8, 10, 12]
    assert lower_bound(0, len(arr), arr, 1) == 0
    assert lower_bound(0, len(arr), arr, 2) == 0
    assert lower_bound(0, len(arr), arr, 10) == 4
    assert lower_bound(0, len(arr), arr, 11) == 5
    assert lower_bound(0, len(arr), arr, 12) == 5
    assert lower_bound(0, len(arr), arr, 13) == 6
    arr = [2, 4, 4, 4, 4, 12]
    assert lower_bound(0, len(arr), arr, 1) == 0
    assert lower_bound(0, len(arr), arr, 2) == 0
    assert lower_bound(0, len(arr), arr, 4) == 1
    assert lower_bound(0, len(arr), arr, 5) == 5
    assert lower_bound(0, len(arr), arr, 12) == 5
    assert lower_bound(0, len(arr), arr, 13) == 6
    arr = [2]
    assert lower_bound(0, len(arr), arr, 2) == 0
    assert lower_bound(0, len(arr), arr, 3) == 1
    # print('lower_bound Tests OK')


def test_upper_bound():
    arr = [2, 4, 6, 8, 10, 12]
    assert upper_bound(0, len(arr), arr, 6) == 3
    assert upper_bound(0, len(arr), arr, 7) == 3
    assert upper_bound(0, len(arr), arr, 1) == 0
    assert upper_bound(0, len(arr), arr, 2) == 1
    assert upper_bound(0, len(arr), arr, 10) == 5
    assert upper_bound(0, len(arr), arr, 11) == 5
    assert upper_bound(0, len(arr), arr, 12) == 6
    assert upper_bound(0, len(arr), arr, 13) == 6
    arr = [2, 4, 4, 4, 4, 12]
    assert upper_bound(0, len(arr), arr, 1) == 0
    assert upper_bound(0, len(arr), arr, 2) == 1
    assert upper_bound(0, len(arr), arr, 4) == 5
    assert upper_bound(0, len(arr), arr, 5) == 5
    assert upper_bound(0, len(arr), arr, 12) == 6
    assert upper_bound(0, len(arr), arr, 13) == 6
    arr = [2]
    assert upper_bound(0, len(arr), arr, 2) == 1
    assert upper_bound(0, len(arr), arr, -1) == 0
    # print('upper_bound Tests OK')


def tests():
    test_lower_bound()
    test_upper_bound()


def check(now, seq_a: list[int], seq_b: list[int]):
    a_lb = lower_bound(0, len(seq_a), seq_a, now)
    a_ub = upper_bound(0, len(seq_a), seq_a, now)
    b_lb = lower_bound(0, len(seq_a), seq_b, now)
    b_ub = upper_bound(0, len(seq_a), seq_b, now)
    lt_x = a_lb + b_lb
    gt_x = len(seq_a) * 2 - a_ub - b_ub
    return lt_x


def median(seq_a: list[int], seq_b: list[int], l):
    left = min(seq_a[0], seq_b[0])
    right = max(seq_a[-1], seq_b[-1])
    while left < right:
        mid = (left + right) // 2
        a_lb = lower_bound(0, l, seq_a, mid)
        a_ub = upper_bound(0, l, seq_a, mid)
        b_lb = lower_bound(0, l, seq_b, mid)
        b_ub = upper_bound(0, l, seq_b, mid)
        lt_x = a_lb + b_lb
        gt_x = len(seq_a) * 2 - a_ub - b_ub
        if lt_x <= l - 1 and gt_x <= l:
            return mid
        elif lt_x > l - 1:
            right = mid
        else:
            left = mid + 1
    return left


def medians(n, l, sequences):
    ans = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans.append(median(sequences[i], sequences[j], l))
    print(*ans, sep='\n')


def main():
    tests()
    medians(*read_input())


if __name__ == '__main__':
    main()
