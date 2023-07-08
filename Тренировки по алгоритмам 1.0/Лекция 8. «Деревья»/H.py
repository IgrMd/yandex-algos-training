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


def is_leaf(root: Node) -> bool:
    return root.left is None and root.right is None


def height(root: Node) -> int:
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_balanced_recursive(root: Node) -> bool:
    if root is None:
        return True
    if is_leaf(root):
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return is_balanced_recursive(root.left) and is_balanced_recursive(root.right)


def is_balanced(items: list):
    root = Node(value=items[0], parent=None)
    for item in items:
        if item == 0:
            break
        add(root, item)
    if is_balanced_recursive(root):
        print('YES')
    else:
        print('NO')


def main():
    is_balanced(read_input())


if __name__ == '__main__':
    main()
