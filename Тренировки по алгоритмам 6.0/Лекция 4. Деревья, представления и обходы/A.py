from collections import defaultdict


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

    def helper(cur_depth, parent):
        ans.append((parent, cur_depth))
        if parent not in node_map:
            return
        for child in node_map[parent]:
            helper(cur_depth + 1, child)

    helper(0, root)
    ans.sort()
    for item in ans:
        print(*item)


def main():
    genealogical_tree(*read_input())


if __name__ == '__main__':
    main()
