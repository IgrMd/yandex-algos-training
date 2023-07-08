from dataclasses import dataclass
import sys

sys.setrecursionlimit(100000)


def read_input():
    n = int(input())
    items = []
    for _ in range(n - 1):
        child_name, parent_name = input().split()
        items.append((child_name, parent_name))
    return items


@dataclass
class Node:
    value: str
    root: any
    descendants: int = 0
    parent: any = None
    left: any = None
    right: any = None


def add(root: Node, key: str) -> Node:
    if key == root.value:
        return root
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key, root=root)
            return root.left
        else:
            return add(root.left, key)
    if key > root.value:
        if root.right is None:
            root.right = Node(value=key, root=root)
            return root.right
        else:
            return add(root.right, key)


def traverse_descendants(root: Node):
    if root.left is not None:
        traverse_descendants(root.left)
    print(root.value, root.descendants)
    if root.right is not None:
        traverse_descendants(root.right)


def calculate_descendants(root: Node):
    if root.left:
        calculate_descendants(root.left)
    if root.right:
        calculate_descendants(root.right)
    if parent_node := root.parent:
        while parent_node:
            parent_node.descendants += 1
            parent_node = parent_node.parent


def descendants(items: list):
    child_name, parent_name = items[0]
    root = Node(value=parent_name, root=None)
    for child_name, parent_name in items:
        parent_node = add(root, parent_name)
        child_node = add(root, child_name)
        child_node.parent = parent_node
    calculate_descendants(root)
    traverse_descendants(root)


def main():
    descendants(read_input())


if __name__ == '__main__':
    main()
