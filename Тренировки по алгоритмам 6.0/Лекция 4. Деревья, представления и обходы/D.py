import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def read_input():
    # requests = []
    # while request := input().strip():
    #     if not request:
    #         break
    #     requests.append(request)
    # return requests

    requests = []
    with open('input.txt', 'r') as file:
        while request := file.readline().strip():
            requests.append(request)
    return requests


def print_tree(root: Node, depth):
    if root is None:
        return
    print_tree(root.left, depth + 1)
    print('.' * depth, end='')
    print(root.val)
    print_tree(root.right, depth + 1)


def add(root: Node, val):
    if root.val == val:
        return False
    if val < root.val:
        if root.left is None:
            root.left = Node(val)
            return True
        return add(root.left, val)
    else:
        if root.right is None:
            root.right = Node(val)
            return True
        return add(root.right, val)


def find(root: Node, val):
    if root is None:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return find(root.left, val)
    else:
        return find(root.right, val)


def binary_search_tree(requests: list[str]):
    root = None
    for request in requests:
        if request == 'PRINTTREE':
            print_tree(root, 0)
            continue

        cmd, val = request.split()
        val = int(val)
        if cmd == 'ADD':
            if root is None:
                root = Node(val)
                print('DONE')
                continue
            if add(root, val):
                print('DONE')
            else:
                print('ALREADY')
        elif cmd == 'SEARCH':
            if find(root, val):
                print('YES')
            else:
                print('NO')


def main():
    binary_search_tree(read_input())


if __name__ == '__main__':
    main()
