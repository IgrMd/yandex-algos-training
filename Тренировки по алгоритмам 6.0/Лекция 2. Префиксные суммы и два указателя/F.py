def read_input():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    return n, nums


MODULO = 1000000007


def sum_triplets_slow(n, nums: list[int]):
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                ans += (nums[i] * nums[j] * nums[k]) % MODULO
    return ans


def sum_triplets_fast(n, nums: list[int]):
    pref_sums = [0] * (n + 1)
    for i in range(n):
        pref_sums[i + 1] = pref_sums[i] + nums[i]
    pre_mult = [0] * n
    for i in range(n):
        pre_mult[i] = nums[i] * (pref_sums[n] - pref_sums[i + 1])
    pref_mult_sums = [0] * (n + 1)
    for i in range(n):
        pref_mult_sums[i + 1] = (pref_mult_sums[i] + pre_mult[i]) % MODULO
    ans = 0
    for i in range(n - 2):
        ans += (nums[i] * (pref_mult_sums[n] - pref_mult_sums[i + 1])) % MODULO
    return ans % MODULO


def main():
    print(sum_triplets_fast(*read_input()))


if __name__ == '__main__':
    main()
