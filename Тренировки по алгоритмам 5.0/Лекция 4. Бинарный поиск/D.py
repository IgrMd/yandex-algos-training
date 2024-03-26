def read_input():
    w, n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    return w, n, m, arr_a, arr_b


MAX_INT = 10 ** 8


def half_report_len(w, arr):
    row_count = 1
    row_len = 0
    for word_len in arr:
        if word_len > w:
            return MAX_INT
        if row_len + word_len <= w:
            row_len += word_len + 1
        else:
            row_count += 1
            row_len = word_len + 1
    return row_count


def report_len(half, w, arr_a, arr_b):
    left = half_report_len(half, arr_a)
    right = half_report_len(w - half, arr_b)
    return max(left, right)


def check_len(half, w, arr_a, arr_b):
    left = half_report_len(half, arr_a)
    right = half_report_len(w - half, arr_b)
    return left <= right


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


def report(w, n, m, arr_a, arr_b):
    l = max(arr_a)
    r = w - max(arr_b)
    if l == r:
        return report_len(l, w, arr_a, arr_b)
    buf = upper_bound(l, r, check_len, (w, arr_a, arr_b))
    ans1 = report_len(buf, w, arr_a, arr_b)
    ans2 = report_len(buf - 1, w, arr_a, arr_b) if buf > l else ans1
    ans3 = report_len(buf + 1, w, arr_a, arr_b) if buf < r else ans1
    return min(ans1, ans2, ans3)


if __name__ == '__main__':
    print(report(*read_input()))
