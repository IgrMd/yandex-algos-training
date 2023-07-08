def read_input():
    n, a, b, w, h = [int(x) for x in input().split()]
    return n, a, b, w, h


def upper_bound(left: int, right: int, check, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, params):
            left = mid
        else:
            right = mid - 1
    return left


def check_protection_d(d, params):
    n, a, b, w, h = params
    w_cnt = w // (a + 2 * d)
    h_cnt = h // (b + 2 * d)
    return n <= w_cnt * h_cnt


def protection_d(n, a, b, w, h):
    d1 = upper_bound(0, min(w, h), check_protection_d, (n, a, b, w, h))
    d2 = upper_bound(0, min(w, h), check_protection_d, (n, a, b, h, w))
    return max(d1, d2)


def main():
    print(protection_d(*read_input()))


if __name__ == '__main__':
    main()
