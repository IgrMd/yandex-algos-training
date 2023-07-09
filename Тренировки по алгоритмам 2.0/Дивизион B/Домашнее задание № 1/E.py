from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def read_input():
    d = int(input())
    x, y = [int(x) for x in input().split()]
    return d, Point(x, y)


def distance_2(p1: Point, p2: Point):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def point_location(d: int, point: Point):
    a = Point(0, 0)
    b = Point(d, 0)
    c = Point(0, d)
    if point.x + point.y <= d and point.x >= 0 and point.y >= 0:
        return 0
    dst_a = distance_2(a, point)
    dst_b = distance_2(b, point)
    dst_c = distance_2(c, point)
    return (min((dst_a, 1), (dst_b, 2), (dst_c, 3)))[1]


def main():
    print(point_location(*read_input()))


if __name__ == '__main__':
    main()
