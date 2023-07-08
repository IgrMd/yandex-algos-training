from collections import defaultdict


def read_input():
    k = int(input())
    s = input()
    return k, s


def find_max_beauty(k, s):
    arr = defaultdict(int)
    max_beauty, largest_count = 0, 0
    for i, c in enumerate(s):
        arr[c] += 1
        largest_count = max(largest_count, arr[c])
        if max_beauty - largest_count >= k:
            arr[s[i - max_beauty]] -= 1
        else:
            max_beauty += 1
    return max_beauty


def main():
    print(find_max_beauty(*read_input()))


if __name__ == '__main__':
    main()
