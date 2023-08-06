def read_input():
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    return n, k, arr


def confuse(arr: list[int]):
    sum_a = sum(arr)
    for i in range(len(arr)):
        arr[i] = sum_a - arr[i]


def process_confuses(n, k, arr: list[int]):
    for _ in range(k):
        confuse(arr)
    return max(arr) - min(arr)


def main():
    print(process_confuses(*read_input()))


if __name__ == '__main__':
    main()
