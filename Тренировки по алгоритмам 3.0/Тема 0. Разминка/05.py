def read_input():
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    return n, lst


def best_string(n, lst):
    if n < 2:
        return 0
    summ = 0
    for i in range(1, n):
        summ += min(lst[i], lst[i - 1])
    return summ


def main():
    print(best_string(*read_input()))


if __name__ == '__main__':
    main()
