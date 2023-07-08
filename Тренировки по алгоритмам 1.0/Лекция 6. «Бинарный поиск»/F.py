def read_input():
    n, x, y = [int(x) for x in input().split()]
    return n, x, y


def lower_bound(left: int, right: int, check_func, params):
    while left < right:
        mid = (left + right) // 2
        if check_func(mid, params):
            right = mid
        else:
            left = mid + 1
    return left


def check_copies(now, params):
    n, x, y = params
    x_printed = now // x
    y_printed = now // y
    return n <= x_printed + y_printed


def min_time_needed(n, x, y):
    min_t = min(x, y)
    n -= 1
    time = lower_bound(0, max(x, y) * n, check_copies, (n, x, y))
    return time + min_t


def main():
    print(min_time_needed(*read_input()))


if __name__ == '__main__':
    main()
