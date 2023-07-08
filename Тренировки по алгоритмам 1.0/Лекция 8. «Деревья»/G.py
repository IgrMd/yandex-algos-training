from dataclasses import dataclass


def read_input():
    items = [int(x) for x in input().split()]
    return items


@dataclass
class Node:
    value: int
    parent: any
    left: any = None
    right: any = None


def add(root: Node, key: int) -> None:
    if key == root.value:
        return
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key, parent=root)
        else:
            add(root.left, key)
    if key > root.value:
        if root.right is None:
            root.right = Node(value=key, parent=root)
        else:
            add(root.right, key)


def traverse_recursive_branches(root: Node) -> None:
    if root.left is not None:
        traverse_recursive_branches(root.left)
    if int(root.left is not None) + int(root.right is not None) == 1:
        print(root.value)
    if root.right is not None:
        traverse_recursive_branches(root.right)


def traverse_branches(items: list):
    root = Node(value=items[0], parent=None)
    for item in items:
        if item == 0:
            break
        add(root, item)
    traverse_recursive_branches(root)


def main():
    traverse_branches(read_input())


if __name__ == '__main__':
    main()
