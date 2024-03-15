from collections import defaultdict


def read_input():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    return n, k, nums


def repeated_num(n, k, nums):
    num_to_index = dict()
    for i, num in enumerate(nums):
        if num not in num_to_index:
            num_to_index[num] = i
        else:
            if i - num_to_index[num] <= k:
                return 'YES'
            else:
                num_to_index[num] = i
    return 'NO'


def main():
    print(repeated_num(*read_input()))


if __name__ == '__main__':
    main()
