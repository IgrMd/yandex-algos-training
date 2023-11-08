def read_input():
    s = input().strip()
    q = int(input().strip())
    requests = [[int(x) for x in input().split()] for _ in range(q)]
    return s, q, requests


X = 257
P = 10 ** 9 + 7


def is_equal(from1, from2, slen, h, x):
    return (
            (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % P ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % P
    )


def string_compare(s, q, requests):
    n = len(s)
    s = ' ' + s
    h = [0] * (n + 1)
    x = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * X + ord(s[i])) % P
        x[i] = (x[i - 1] * X) % P

    for l, a, b in requests:
        print('yes' if is_equal(a + 1, b + 1, l, h, x) else 'no')


def main():
    string_compare(*read_input())


if __name__ == '__main__':
    main()
