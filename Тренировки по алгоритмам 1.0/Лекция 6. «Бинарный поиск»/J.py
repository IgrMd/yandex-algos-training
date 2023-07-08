def read_input():
    n, l = [int(x) for x in input().split()]
    sequences = [[int(x) for x in input().split()] for _ in range(n)]
    return n, l, sequences


def median(sequence_a: list[int], sequence_b: list[int], l):
    left = right = 0
    mem = 0
    while left + right < l:
        if sequence_b[right] < sequence_a[left]:
            mem = sequence_b[right]
            right += 1
        else:
            mem = sequence_a[left]
            left += 1
    return mem


def medians(n, l, sequences):
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(median(sequences[i], sequences[j], l))


def main():
    medians(*read_input())


if __name__ == '__main__':
    main()
