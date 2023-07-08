from collections import defaultdict


def read_input():
    n, k = [int(x) for x in input().split()]
    trees = [int(x) for x in input().split()]
    return n, k, trees


def coords(n, k, trees):
    trees_met = defaultdict(int)
    inf = 10 ** 6
    prev = [inf] * (n + 1)
    l = r = 0
    while r < n:
        while r < n and len(trees_met) < k:
            trees_met[trees[r]] += 1
            r += 1
        while l < r and len(trees_met) == k:
            trees_met[trees[l]] -= 1
            if trees_met[trees[l]] == 0:
                trees_met.pop(trees[l])
            l += 1
            prev[r] = l

    min_interval = inf
    answer = (1, n)
    for i in range(1, n + 1):
        if prev[i] != inf and i - prev[i] < min_interval:
            min_interval = i - prev[i]
            answer = (prev[i], i)
    return answer


def main():
    print(*coords(*read_input()))


if __name__ == '__main__':
    main()
