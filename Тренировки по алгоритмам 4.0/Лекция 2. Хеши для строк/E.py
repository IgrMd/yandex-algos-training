# X = 10
X = 257
P = 10 ** 9 + 7


def read_input():
    s = input().strip()
    s = '`' + '`'.join(s) + '`'
    sr = s[::-1]
    return s, sr


def prepare_data(s: str, sr: str):
    n = len(s)
    h = [0] * (n + 1)
    hr = [0] * (n + 1)
    x = [1] * (n + 1)
    for i in range(n):
        h[i] = (h[i - 1] * X + ord(s[i])) % P
        hr[i] = (hr[i - 1] * X + ord(sr[i])) % P
    for i in range(1, n + 1):
        x[i] = (x[i - 1] * X) % P
    return h, hr, x


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


def palindrome_count(s: str, sr: str):
    n = len(s)
    h, hr, x = prepare_data(s, sr)
    answer = 0
    for curr_i in range(n):
        curr_ir = n - curr_i - 1
        p_len = upper_bound(1, min(curr_i + 1, curr_ir + 1), is_equal, (curr_i, curr_ir, h, hr, x))
        answer += p_len // 2
    return answer


def main():
    print(palindrome_count(*read_input()))


if __name__ == '__main__':
    main()
