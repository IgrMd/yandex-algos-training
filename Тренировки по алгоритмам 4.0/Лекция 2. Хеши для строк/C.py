X = 257
P = 10 ** 9 + 7


def read_input():
    return input()


def is_equal(slen, from1, from2, h, x):
    if slen == 0:
        return True
    return (
            (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % P ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % P
    )


def upper_bound(left: int, right: int, check, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, *params):
            left = mid
        else:
            right = mid - 1
    return left


def string_base_len(s):
    n = len(s)
    h = [0] * (n + 1)
    x = [1] * (n + 1)
    for i in range(n):
        h[i] = (h[i - 1] * X + ord(s[i])) % P
    for i in range(1, n + 1):
        x[i] = (x[i - 1] * X) % P
    z = [0] * n
    for i in range(1, n):
        if s[i] == s[0]:
            z[i] = upper_bound(1, n - i, is_equal, (0, i, h, x))
    return z


def main():
    print(*string_base_len(read_input()))


if __name__ == '__main__':
    main()
