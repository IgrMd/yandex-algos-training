def waiting_time(a, b, n, m):
    max_a = n + a * (n + 1)
    min_a = n + a * (n - 1)
    max_b = m + b * (m + 1)
    min_b = m + b * (m - 1)
    a_not_ok = min_a > max_b or max_a < min_b
    b_not_ok = min_b > max_a or max_b < min_a
    if a_not_ok or b_not_ok:
        return (-1,)
    return max(min_a, min_b), min(max_a, max_b)


assert waiting_time(1, 3, 3, 2) == (5, 7)
assert waiting_time(1, 5, 1, 2) == (-1,)
assert waiting_time(5, 3, 4, 5) == (19, 23)


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    m = int(input())
    print(*waiting_time(a, b, n, m))


if __name__ == '__main__':
    main()
