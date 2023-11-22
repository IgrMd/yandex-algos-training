def read_input():
    n = int(input().strip())
    return n


def generate(arr: list, t: int, mask: int):
    if t == len(arr):
        print(*arr, sep='')
        return
    for i in range(1, len(arr) + 1):
        if not mask & (1 << i):
            arr[t] = i
            generate(arr, t + 1, mask | (1 << i))


def all_permutations(n):
    arr = [i for i in range(1, n + 1)]
    generate(arr, 0, 0)


def main():
    all_permutations(read_input())


if __name__ == '__main__':
    main()
