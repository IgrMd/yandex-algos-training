def read_input():
    nums = []
    x = int(input())
    while x != 0:
        nums.append(x)
        x = int(input())
    return nums


def max_num_count(nums: list[int]):
    if not len(nums):
        return 0
    max_num = nums[0]
    count = 0
    for num in nums:
        if num == max_num:
            count += 1
        if num > max_num:
            max_num = num
            count = 1
    return count


def main():
    print(max_num_count(read_input()))


if __name__ == '__main__':
    main()
