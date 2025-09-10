from collections import defaultdict


def read_input():
    n, k = [int(x) for x in input().split()]
    trees = [int(x) for x in input().split()]
    return n, k, trees


def coords(n, k, trees):
    trees_met = defaultdict(int)
    l_ans, r_ans = 0, n - 1
    l = 0
    for r in range(n):
        trees_met[trees[r]] += 1
        while len(trees_met) == k:
            if r - l < r_ans - l_ans:
                r_ans, l_ans = r, l
            trees_met[trees[l]] -= 1
            if trees_met[trees[l]] == 0:
                trees_met.pop(trees[l])
            l += 1
    return l_ans + 1, r_ans + 1


def main():
    print(*coords(*read_input()))


if __name__ == '__main__':
    main()
