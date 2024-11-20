from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []


def read_input():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        node_map = defaultdict(list)
        children = set()
        for _ in range(n - 1):
            child, parent = file.readline().split()
            node_map[parent].append(child)
            children.add(child)
        root = None
        for parent in node_map.keys():
            if parent not in children:
                root = parent
                break
        requests = []
        while request := file.readline():
            requests.append(request.split())
    return root, node_map, requests


time = 0


def genealogical_tree(root, node_map, requests):
    buf = {}

    def helper(now):
        global time
        time += 1
        if now not in node_map:
            buf[now] = (time, time)
            return
        time_in = time
        for child in node_map[now]:
            helper(child)
        buf[now] = (time_in, time)

    helper(root)
    for child1, child2 in requests:
        t1 = min(buf[child1][0], buf[child2][0])
        t2 = max(buf[child1][1], buf[child2][1])
        ans = ''
        t1_max = 0
        for parent, times in buf.items():
            if times[0] <= t1 and times[1] >= t2:
                if t1 > t1_max:
                    t1_max = t1
                    ans = parent
        print(ans)


def main():
    genealogical_tree(*read_input())


if __name__ == '__main__':
    main()
