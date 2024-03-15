from collections import defaultdict


def read_input():
    n = int(input())
    nums = list(map(int, input().split()))
    return n, nums


def min_count_to_delete(n, nums):
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    ans = 0
    for num, count in counts.items():
        if num + 1 in counts:
            ans = max(ans, counts[num + 1] + count)
        else:
            ans = max(ans, count)
    return n - ans


def main():
    print(min_count_to_delete(*read_input()))


if __name__ == '__main__':
    main()
