def read_input():
    return input().strip()


X = 257
P = 10 ** 9 + 7


def is_equal(from1, from2, slen, h, x):
    return (
            (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % P ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % P
    )


def string_base_len(s):
    n = len(s)
    s = ' ' + s
    h = [0] * (n + 1)
    x = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * X + ord(s[i])) % P
        x[i] = (x[i - 1] * X) % P
    max_equal_len = 0
    for cur_equal_len in range(1, n):
        if is_equal(1, n + 1 - cur_equal_len, cur_equal_len, h, x):
            max_equal_len = max(max_equal_len, cur_equal_len)
    if max_equal_len == 0:
        return n
    else:
        return n - max_equal_len


def main():
    print(string_base_len(read_input()))


if __name__ == '__main__':
    main()
