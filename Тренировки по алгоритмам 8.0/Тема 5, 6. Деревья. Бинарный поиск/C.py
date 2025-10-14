def read_input():
    n, w, h = map(int, input().split())
    words = []
    for _ in range(n):
        a, b = map(int, input().split())
        words.append((a, b))
    return n, w, h, words


def float_bin_search(left: float, right: float, cmp):
    eps = float('1e-7')

    prev_mid = right
    while True:
        mid = (left + right) / 2
        if not cmp(mid):
            right = mid
        else:
            left = mid
        if abs(prev_mid - mid) / prev_mid < eps:
            break
        prev_mid = mid
    return prev_mid


A = 0
B = 1


def advertisement(n: int, w: int, h: int, words: list[tuple[int]]):
    def cmp(k):
        i = 0
        sum_h = 0
        while i < n:
            sum_w = words[i][A] * k
            if sum_w > w:
                return False
            b_prev = words[i][B]
            i += 1
            while i < n and words[i][B] == b_prev and sum_w + words[i][A] * k < w:
                sum_w += words[i][A] * k
                i += 1
            sum_h += b_prev * k
            if sum_h > h:
                break
        return sum_h <= h

    left = min(w / sum(x[A] for x in words), h / sum(x[B] for x in words))
    right = max(w / max(x[A] for x in words), h / max(x[B] for x in words))

    return float_bin_search(left, right, cmp)


def main():
    print(advertisement(*read_input()))


if __name__ == '__main__':
    main()
