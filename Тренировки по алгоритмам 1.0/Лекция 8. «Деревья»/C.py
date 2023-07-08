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


def find_max(root: Node) -> Node:
    if root.right is None:
        return root
    return find_max(root.right)


def second_max(items: list):
    root = Node(value=items[0], parent=None)
    for item in items:
        if item == 0:
            break
        add(root, item)
    max_node = find_max(root)
    if max_node.left is None:
        return max_node.parent.value
    else:
        return find_max(max_node.left).value


def main():
    print(second_max(read_input()))


if __name__ == '__main__':
    main()
