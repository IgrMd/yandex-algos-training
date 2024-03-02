def read_input():
    n, k, d = list(map(int, input().split()))
    return n, k, d


def startup(n, k, d):
    num = None
    for i in range(10):
        if (n * 10 + i) % k == 0:
            num = n * 10 + i
            break
    if not num:
        return -1
    return str(num) + '0' * (d - 1)


def main():
    print(startup(*read_input()))


if __name__ == '__main__':
    main()
