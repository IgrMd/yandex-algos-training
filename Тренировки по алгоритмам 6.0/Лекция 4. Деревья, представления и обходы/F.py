from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)


def read_input():
    n = int(input().strip())
    node_map = defaultdict(list)
    for i, parent in enumerate(input().split(), 1):
        parent = int(parent) - 1
        node_map[parent].append(i)
    return n, node_map


def burocracy(n, node_map):
    ans = [0] * n

    def helper(cur_v) -> tuple[int, int]:
        if cur_v not in node_map:
            ans[cur_v] = 1
            return 1, 1
        sum_child_coins, sum_subtree_count = 0, 0
        for child in node_map[cur_v]:
            coin, subtree_count = helper(child)
            sum_child_coins += coin
            sum_subtree_count += subtree_count
        coins = sum_child_coins + sum_subtree_count + 1
        ans[cur_v] = coins
        return coins, sum_subtree_count + 1

    helper(0)
    return ans


def main():
    print(*burocracy(*read_input()))


if __name__ == '__main__':
    main()
