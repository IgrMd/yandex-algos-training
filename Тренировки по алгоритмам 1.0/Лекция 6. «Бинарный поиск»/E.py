def read_input():
    a = int(input())
    b = int(input())
    c = int(input())
    return a, b, c


def lower_bound(left: int, right: int, check_func, params):
    while left < right:
        mid = (left + right) // 2
        if check_func(mid, params):
            right = mid
        else:
            left = mid + 1
    return left


def check_marks(d, params):
    a, b, c = params
    return 2 * (a * 2 + b * 3 + c * 4 + d * 5) >= 7 * (a + b + c + d)


def marks_count(a, b, c):
    count = lower_bound(0, a + b + c, check_marks, (a, b, c))
    return count


def main():
    print(marks_count(*read_input()))


if __name__ == '__main__':
    main()
