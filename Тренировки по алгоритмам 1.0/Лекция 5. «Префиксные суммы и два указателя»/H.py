from collections import defaultdict


def read_input():
    n, k = [int(x) for x in input().split()]
    s = input()
    return n, k, s


def max_substr(n, k, s):
    symbols = defaultdict(int)
    l = 0
    r = 0
    l_mem = len_mem = 0
    while l <= r < n:
        if symbols[s[r]] < k:
            symbols[s[r]] += 1
            if len_mem < r - l + 1:
                l_mem = l
                len_mem = r - l + 1
            r += 1
            continue
        while l < r and symbols[s[r]] >= k:
            symbols[s[l]] -= 1
            l += 1

    return len_mem, l_mem + 1


def main():
    print(*max_substr(*read_input()))


if __name__ == '__main__':
    main()
