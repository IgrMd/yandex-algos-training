from dataclasses import dataclass
from itertools import permutations


@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def read_input():
    n = int(input())
    requests = [[] for _ in range(n)]
    for i in range(n):
        coords = [int(x) for x in input().split()]
        for j in range(0, len(coords), 2):
            requests[i].append(Point(coords[j], coords[j + 1]))
    return n, requests


def is_parallelogram(points):
    a, b, c, d = points
    ab = b - a
    cd = d - c
    if ab != cd:
        return False
    ac = c - a
    bd = d - b
    if ac != bd:
        return False
    return True


def check(request: list[Point]):
    points_permutations = list(permutations(request))
    for points in points_permutations:
        if is_parallelogram(points):
            return True
    return False


def parallelograms(n, requests: list[list]):
    for request in requests:
        if check(request):
            print('YES')
        else:
            print('NO')


def main():
    parallelograms(*read_input())


if __name__ == '__main__':
    main()
