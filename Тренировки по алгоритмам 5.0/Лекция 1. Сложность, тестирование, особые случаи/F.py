def read_input():
    n = int(input())
    nums = list(map(abs, map(int, input().split())))
    return n, nums


def operators(n, nums):
    even_count, odd_count = 0, 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    need_x = odd_count % 2 == 0
    answer = []
    for i in range(1, n):
        if nums[i] % 2 != 0 and need_x:
            answer.append(chr(120))
            need_x = False
        else:
            answer.append(chr(43))
    return ''.join(answer)


def main():
    print(operators(*read_input()))


if __name__ == '__main__':
    main()
