def read_input():
    n, k = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    return n, k, arr1, arr2


def lower_bound(left: int, right: int, less_cmp, params):
    right -= 1
    while left < right:
        mid = (left + right) // 2
        if less_cmp(mid, params):
            left = mid + 1
        else:
            right = mid
    if less_cmp(left, params):
        left += 1
    return left


def comparator(i, params):
    arr, value = params
    return arr[i] < value


def bin_search(n: int, k: int, arr1: list[int], arr2: list[int]):
    arr1.sort()
    for item in arr2:
        index = lower_bound(0, len(arr1), comparator, (arr1, item))
        found = index != len(arr1) and arr1[index] == item
        if found:
            print('YES')
        else:
            print('NO')


def test():
    arr = [2, 4, 6, 8, 10, 12]
    assert lower_bound(0, len(arr), comparator, (arr, 1)) == 0
    assert lower_bound(0, len(arr), comparator, (arr, 2)) == 0
    assert lower_bound(0, len(arr), comparator, (arr, 10)) == 4
    assert lower_bound(0, len(arr), comparator, (arr, 11)) == 5
    assert lower_bound(0, len(arr), comparator, (arr, 12)) == 5
    assert lower_bound(0, len(arr), comparator, (arr, 13)) == 6
    arr = [2, 4, 4, 4, 4, 12]
    assert lower_bound(0, len(arr), comparator, (arr, 1)) == 0
    assert lower_bound(0, len(arr), comparator, (arr, 2)) == 0
    assert lower_bound(0, len(arr), comparator, (arr, 4)) == 1
    assert lower_bound(0, len(arr), comparator, (arr, 5)) == 5
    assert lower_bound(0, len(arr), comparator, (arr, 12)) == 5
    assert lower_bound(0, len(arr), comparator, (arr, 13)) == 6
    # print('Tests OK')


def main():
    test()
    bin_search(*read_input())


if __name__ == '__main__':
    main()
