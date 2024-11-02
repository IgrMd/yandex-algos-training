def read_input():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    return n, nums


def delete_medians(n, nums: list[int]):
    ans = []
    nums.sort()
    l = (len(nums) - 1) // 2
    r = l + 1
    while len(ans) != n:
        if l + 1 > n - r:
            ans.append(nums[l])
            l -= 1
            continue
        if l + 1 < n - r:
            ans.append(nums[r])
            r += 1
            continue
        if nums[l] <= nums[r]:
            ans.append(nums[l])
            l -= 1
        else:
            ans.append(nums[r])
            r += 1
    return ans


def main():
    print(*delete_medians(*read_input()))


if __name__ == '__main__':
    main()
