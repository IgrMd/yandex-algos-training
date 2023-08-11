def read_input():
    nums1 = set(map(int, input().split()))
    nums2 = set(map(int, input().split()))
    return nums1, nums2


def same_nums(nums1: set[int], nums2: set[int]):
    return len(nums1.intersection(nums2))


def main():
    print(same_nums(*read_input()))


if __name__ == '__main__':
    main()
