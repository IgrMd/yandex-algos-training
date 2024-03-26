def read_input():
    n = int(input())
    return n


def check_ships(k, n):
    n += 1
    sum = 0
    for i in range(1, k + 1):
        next = (i + 1) * (k - i + 1)
        if n - sum < next:
            return False
        sum += next
    return True


def lower_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r + 1) // 2
        if cmp(mid, *params):
            l = mid
        else:
            r = mid - 1
    return l


def execute(n):
    ans = lower_bound(0, (n + 1) // 2, check_ships, (n,))
    return ans


if __name__ == '__main__':
    print(execute(read_input()))
