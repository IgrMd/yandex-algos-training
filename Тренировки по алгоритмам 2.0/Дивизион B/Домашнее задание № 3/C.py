from collections import defaultdict


def read_input():
    nums = list(map(int, input().split()))
    return nums


def meet_num(nums: list[int]):
    mem = defaultdict(int)
    for num in nums:
        mem[num] += 1
    return [key for key, value in mem.items() if value == 1]


def main():
    print(*meet_num(read_input()))


if __name__ == '__main__':
    main()
