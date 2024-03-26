def read_input():
    n = int(input())
    return n


MAX_INT = 10 ** 10


def sum_first(n):
    return (n * (n + 1)) // 2


def check_diagonal(i, n):
    return n <= sum_first(i)


def upper_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    if not cmp(l, *params):
        l += 1
    return l


def rational(n):
    diag_n = upper_bound(1, MAX_INT, check_diagonal, (n,))
    diag_i = n - sum_first(diag_n - 1) - 1
    i, j = diag_n, 1
    if diag_n % 2:
        i, j = j, i
    if diag_n % 2:
        i += diag_i
        j -= diag_i
    else:
        i -= diag_i
        j += diag_i
    return '/'.join((str(i), str(j)))


if __name__ == '__main__':
    print(rational(read_input()))
