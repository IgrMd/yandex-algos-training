def read_input():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    return n, k, nums


def lucky_pairs(n, k, nums):
    pref_sums = [0] * (n + 1)
    for i in range(n):
        pref_sums[i + 1] = pref_sums[i] + nums[i]
    r = 0
    ans = 0
    for l in range(len(pref_sums)):
        while r < n and pref_sums[r] - pref_sums[l] < k:
            r += 1
        if pref_sums[r] - pref_sums[l] == k:
            ans += 1
    return ans


def main():
    print(lucky_pairs(*read_input()))


if __name__ == '__main__':
    main()
