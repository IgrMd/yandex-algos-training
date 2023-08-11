from collections import defaultdict


def read_input():
    nums = list(map(int, input().split()))
    return nums


def unique_elements(nums: list[int]):
    mem = defaultdict(int)
    for num in nums:
        mem[num] += 1
    return [key for key, value in mem.items() if value == 1]


def main():
    print(*unique_elements(read_input()))


if __name__ == '__main__':
    main()
