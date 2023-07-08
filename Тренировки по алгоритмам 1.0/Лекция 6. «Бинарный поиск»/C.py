def read_input():
    w, h, n = [int(x) for x in input().split()]
    return w, h, n


def lower_bound(left: int, right: int, check, params):
    while left < right:
        mid = (left + right) // 2
        if check(mid, params):
            right = mid
        else:
            left = mid + 1
    return left


def check_sq_side(a, params):
    w, h, n = params
    w_cnt = a // w
    h_cnt = a // h
    return n <= w_cnt * h_cnt


def bin_search(w, h, n):
    a = lower_bound(0, min(w, h) * n + 1, check_sq_side, (w, h, n))
    return a


def main():
    print(bin_search(*read_input()))


if __name__ == '__main__':
    main()
