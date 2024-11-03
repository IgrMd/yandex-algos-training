def read_input():
    n, c = list(map(int, input().split()))
    s = input().strip()
    return n, c, s


def good_string(n, c, s: str):
    ans = 0
    a = 0
    b = 0
    r = 0
    curr_rudeness = 0
    for l in range(n):
        while r < n and curr_rudeness <= c:
            if s[r] == 'a':
                a += 1
            if s[r] == 'b':
                b += 1
                curr_rudeness += a
            r += 1
        if curr_rudeness > c:
            ans = max(ans, r - l - 1)
        else:
            ans = max(ans, r - l)

        if s[l] == 'a':
            curr_rudeness -= b
            a -= 1
        if s[l] == 'b':
            b -= 1
    return ans


def test():
    assert good_string(3, 1, 'aab') == 2
    assert good_string(6, 2, 'aabcbb') == 4
    assert good_string(2, 1, 'ab') == 2


def main():
    test()
    print(good_string(*read_input()))


if __name__ == '__main__':
    main()
