from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Edge:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        if (self.b.x, self.b.y) < (self.a.x, self.a.y):
            self.a, self.b = self.b, self.a
        self.dx = self.b.x - self.a.x
        self.dy = self.b.y - self.a.y


def read_input():
    n = int(input())
    matches_a = []
    matches_b = []
    for _ in range(n):
        ax, ay, bx, by = map(int, input().split())
        matches_a.append(Edge(Point(ax, ay), Point(bx, by)))
    for _ in range(n):
        ax, ay, bx, by = map(int, input().split())
        matches_b.append(Edge(Point(ax, ay), Point(bx, by)))
    return n, matches_a, matches_b


def matches(n, matches_a: list[Edge], matches_b: list[Edge]):
    offset_map = defaultdict(int)
    for edge_a in matches_a:
        for edge_b in matches_b:
            if edge_a.dx == edge_b.dx and edge_a.dy == edge_b.dy:
                offset_map[(edge_b.a.x - edge_a.a.x, edge_b.a.y - edge_a.a.y)] += 1
    if not len(offset_map):
        return n
    return n - max(offset_map.values())


def main():
    print(matches(*read_input()))


if __name__ == '__main__':
    main()
