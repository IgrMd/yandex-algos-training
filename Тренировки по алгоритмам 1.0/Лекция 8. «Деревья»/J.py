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
    descendants: []
    height: int = 0
    parent: any = None
    left: any = None
    right: any = None


def add(root: Node, key: str) -> Node:
    if key == root.value:
        return root
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key, root=root, descendants=[])
            return root.left
        else:
            return add(root.left, key)
    if key > root.value:
        if root.right is None:
            root.right = Node(value=key, root=root, descendants=[])
            return root.right
        else:
            return add(root.right, key)


def traverse_descendants(root: Node):
    if root.left is not None:
        traverse_descendants(root.left)
    print(root.value, root.height)
    if root.right is not None:
        traverse_descendants(root.right)


def calculate_genealogical_heights(root: Node, curr_height):
    root.height = curr_height
    for descendant in root.descendants:
        calculate_genealogical_heights(descendant, curr_height + 1)


def descendants(items: list):
    child_name, parent_name = items[0]
    root = Node(value=parent_name, root=None, descendants=[])
    for child_name, parent_name in items:
        parent_node = add(root, parent_name)
        child_node = add(root, child_name)
        child_node.parent = parent_node
        parent_node.descendants.append(child_node)
    genealogical_root = root
    while genealogical_root.parent:
        genealogical_root = genealogical_root.parent
    calculate_genealogical_heights(genealogical_root, 0)
    traverse_descendants(root)


def main():
    descendants(read_input())


if __name__ == '__main__':
    main()
