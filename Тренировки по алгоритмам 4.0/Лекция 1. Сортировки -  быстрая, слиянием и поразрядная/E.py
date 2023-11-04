def read_input():
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    return n, arr


def print_arr(title, arr):
    print(f'{title}:')
    print(*arr, sep=', ')


def squash_buckets(buckets: list[list], arr: list):
    arr.clear()
    for i, bucket in enumerate(buckets):
        print(f'Bucket {i}: ', end='')
        if not len(bucket):
            print('empty')
        else:
            print(*bucket, sep=', ')
            for item in bucket:
                arr.append(item)


def sort(n, arr):
    print_arr('Initial array', arr)
    print('**********')
    displ = ord('0')
    item_len = len(arr[0])
    for digit in range(1, item_len + 1):
        print(f'Phase {digit}')
        buckets = [[] for _ in range(10)]
        for s in arr:
            c = ord(s[item_len - digit]) - displ
            buckets[c].append(s)
        squash_buckets(buckets, arr)
        print('**********')
    print_arr('Sorted array', arr)


def main():
    sort(*read_input())


if __name__ == '__main__':
    main()
