X = 257
P = 10 ** 9 + 7


def read_input():
    n = int(input().strip())
    s = input().strip()
    return n, s


def is_equal(slen, from1, from2, h, hr, x):
    if slen == 0:
        return True
    return (
            (h[from1 + slen - 1] - h[from1 - 1] * x[slen]) % P ==
            (hr[from2 + slen - 1] - hr[from2 - 1] * x[slen]) % P
    )


def upper_bound(left: int, right: int, check, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, *params):
            left = mid
        else:
            right = mid - 1
    return left




def string_base_len(n, s: str):
    sr = s[::-1]
    n = len(s)
    h = [0] * (n + 1)
    hr = [0] * (n + 1)
    x = [1] * (n + 1)
    for i in range(n):
        h[i] = (h[i - 1] * X + ord(s[i])) % P
    for i in range(n):
        hr[i] = (hr[i - 1] * X + ord(sr[i])) % P
    for i in range(1, n + 1):
        x[i] = (x[i - 1] * X) % P
    z = [0] * n
    for i in range(1, n):
        # if s[i] == sr[0]:
        z[i] = upper_bound(0, n - i, is_equal, (0, n - i, h, hr, x))
    print(*z, sep=' ')


def main():
    string_base_len(*read_input())


if __name__ == '__main__':
    main()
