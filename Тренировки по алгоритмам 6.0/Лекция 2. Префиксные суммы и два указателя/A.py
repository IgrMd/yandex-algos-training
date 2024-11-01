def read_input():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    return n, nums


def pref_sums(n, nums):
    ans = [nums[0]] * n
    for i in range(1, n):
        ans[i] = ans[i - 1] + nums[i]
    return ans


def main():
    print(*pref_sums(*read_input()))


if __name__ == '__main__':
    main()
