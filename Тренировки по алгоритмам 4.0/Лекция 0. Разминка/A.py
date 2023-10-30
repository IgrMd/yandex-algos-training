def read_input():
    n, m = [int(x) for x in input().split()]
    seq = [int(x) for x in input().split()]
    requests = []
    for _ in range(m):
        requests.append([int(x) for x in input().split()])
    return seq, requests


def find_not_min(l, r, seq):
    now = seq[l]
    for elem in seq[l:r + 1]:
        if elem < now:
            return now
        if elem > now:
            return elem
    return None


def min_in_range(seq, requests):
    for l, r in requests:
        elem = find_not_min(l, r, seq)
        if elem:
            print(elem)
        else:
            print('NOT FOUND')


def main():
    min_in_range(*read_input())


if __name__ == '__main__':
    main()
