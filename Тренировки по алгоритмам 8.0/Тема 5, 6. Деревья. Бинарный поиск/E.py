from collections import defaultdict


def read_input():
    n = int(input().strip())
    graph = defaultdict(list)
    for i in range(1, n):
        ancestor = int(input().strip())
        graph[ancestor].append(i)
    budgets = list(map(int, input().split()))
    return n, graph, budgets


def feudal_reform(n: int, graph: dict[list[int]], budgets: list[int]):
    def helper(curr):
        ans, diff = 0, 0
        for son in graph[curr]:
            ans1, diff1 = helper(son)
            ans += ans1
            diff += diff1
        budgets[curr] += diff
        diff -= budgets[curr]
        ans += abs(budgets[curr])
        return ans, diff

    ans, diff = helper(0)
    return ans


def main():
    print(feudal_reform(*read_input()))


if __name__ == '__main__':
    main()
