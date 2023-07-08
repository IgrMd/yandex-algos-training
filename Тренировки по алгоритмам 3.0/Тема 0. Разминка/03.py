def lower_bound(arr, target, begin, end):
    if end - begin < 2:
        return begin if target <= arr[begin] else end
    mid = (begin + end) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return lower_bound(arr, target, begin, mid)
    else:
        return lower_bound(arr, target, mid, end)


def stickers_count(diego, k, size) -> int:
    i = lower_bound(diego, k, 0, size)
    if i == len(diego):
        return i
    if i == 0:
        return 1 if diego[i] < k else 0
    return i


def main():
    n = int(input())
    diego = sorted(set([int(x) for x in input().split()]))
    k = int(input())
    size = len(diego)
    kl = [int(x) for x in input().split()]
    for k in kl:
        print(stickers_count(diego, k, size))


if __name__ == '__main__':
    main()
