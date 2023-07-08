from dataclasses import dataclass


def read_input():
    items = [int(x) for x in input().split()]
    return items


@dataclass
class Node:
    value: int = None
    left: any = None
    right: any = None


def add(root: Node, key: int, curr_height: int) -> int:
    if key == root.value:
        return -1
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key)
            return curr_height + 1
        else:
            return add(root.left, key, curr_height + 1)
    if key > root.value:
        if root.right is None:
            root.right = Node(value=key)
            return curr_height + 1
        else:
            return add(root.right, key, curr_height + 1)


def tree_heights(items: list):
    root = Node(value=items[0])
    heights = [1]
    for item in items:
        if item == 0:
            break
        curr_height = add(root, item, 1)
        if curr_height != -1:
            heights.append(curr_height)
    return heights


def main():
    print(*tree_heights(read_input()))


if __name__ == '__main__':
    main()
