from collections import defaultdict


def read_input():
    n = int(input().strip())
    tree = defaultdict(lambda: list())
    children = set()
    for _ in range(n - 1):
        child, parent = input().split()
        children.add(child)
        tree[parent].append(child)
    for root in tree.keys():
        if root not in children:
            break
    return n, tree, root


def genealogy(n, tree: dict[str: list[str]], root: str):
    ans = dict()

    def height(root, level):
        ans[root] = level
        for child in tree[root]:
            height(child, level + 1)

    height(root, 0)
    return sorted(ans.items())


def main():
    for row in genealogy(*read_input()):
        print(*row, sep=' ')


if __name__ == '__main__':
    main()
