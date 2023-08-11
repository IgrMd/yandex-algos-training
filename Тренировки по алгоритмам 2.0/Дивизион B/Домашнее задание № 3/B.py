def read_input():
    nums = list(map(int, input().split()))
    return nums


def meet_num(nums: list[int]):
    mem = set()
    for num in nums:
        if num in mem:
            print('YES')
        else:
            mem.add(num)
            print('NO')


def main():
    meet_num(read_input())


if __name__ == '__main__':
    main()
