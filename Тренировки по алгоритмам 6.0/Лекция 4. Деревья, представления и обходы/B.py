from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []


def read_input():
    n = int(input().strip())
    node_map = defaultdict(list)
    children = set()
    for _ in range(n - 1):
        child, parent = input().split()
        node_map[parent].append(child)
        children.add(child)
    root = None
    for parent in node_map.keys():
        if parent not in children:
            root = parent
            break
    return root, node_map


def genealogical_tree(root, node_map):
    ans = []

    def helper(parent) -> int:
        if parent not in node_map:
            ans.append((parent, 0))
            return 0
        successors_count = len(node_map[parent])
        for child in node_map[parent]:
            successors_count += helper(child)
        ans.append((parent, successors_count))
        return successors_count

    helper(root)
    ans.sort()
    for item in ans:
        print(*item)


def main():
    genealogical_tree(*read_input())


if __name__ == '__main__':
    main()
