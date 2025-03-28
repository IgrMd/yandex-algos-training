from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def read_input():
    v = int(input().strip())
    node_map = defaultdict(list)
    for _ in range(v - 1):
        v1, v2 = map(int, input().split())
        v1 -= 1
        v2 -= 1
        node_map[v1].append(v2)
        node_map[v2].append(v1)
    return v, node_map


def subtree_size(v, node_map):
    ans = [0] * v

    def helper(cur_v) -> int:
        if ans[cur_v]:
            return 0
        ans[cur_v] = 1
        for child in node_map[cur_v]:
            ans[cur_v] += helper(child)
        return ans[cur_v]

    helper(0)
    return ans


def main():
    print(*subtree_size(*read_input()))


if __name__ == '__main__':
    main()
