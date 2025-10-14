def read_input():
    a, b, s = map(int, input().split())
    return a, b, s


def bin_search(left: int, right: int, cmp):
    while left < right:
        mid = (left + right) // 2
        if cmp(mid):
            right = mid
        else:
            left = mid + 1
    return left


def shelf(a, b, s):
    def cmp(L):
        return L * L >= s + a * L + b * L - a * b

    L = bin_search(max(a, b) + 1, s + max(a, b) + 1, cmp)
    return L if L * L == s + a * L + b * L - a * b else -1


def main():
    print(shelf(*read_input()))


if __name__ == '__main__':
    main()
