class Point:
    def __init__(self, x=None, y=None, s=None):
        if s is None:
            self.x, self.y = x, y
        else:
            self.x, self.y = [int(x) for x in s.split()]

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash(self.x) * 63 + hash(self.y) * 63 * 63

    def __repr__(self):
        return f'{self.x} {self.y}'


def read_input():
    t, d, n = [int(x) for x in input().split()]
    navigator_reqs = [Point(None, None, input()) for _ in range(n)]
    return t, d, n, navigator_reqs


def manhattan_distance(point1: Point, point2: Point):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def intersect(rect1, rect2):
    return max(rect1[0], rect2[0]), min(rect1[1], rect2[1]), max(rect1[2], rect2[2]), min(rect1[3], rect2[3])


def expand(rect, d):
    minXplusY, maxXplusY, minXminusY, maxXminusY = rect  # min x+y, max x+y, min x-y, max x-y
    return minXplusY - d, maxXplusY + d, minXminusY - d, maxXminusY + d


def manhattan_walk(t, d, n, navigator_reqs: list[Point]):
    boy_rect = (0, 0, 0, 0)
    for pos in navigator_reqs:
        boy_rect = expand(boy_rect, t)
        nav_rect = expand((pos.x + pos.y, pos.x + pos.y, pos.x - pos.y, pos.x - pos.y), d)
        boy_rect = intersect(boy_rect, nav_rect)

    answer = []
    minXplusY, maxXplusY, minXminusY, maxXminusY = boy_rect
    for XplusY in range(minXplusY, maxXplusY + 1):
        for XminusY in range(minXminusY, maxXminusY + 1):
            if (XplusY + XminusY) % 2 == 0:
                x = (XplusY + XminusY) // 2
                y = XplusY - x
                answer.append(Point(x, y))
    return answer


def main():
    boy_points = manhattan_walk(*read_input())
    print(len(boy_points))
    print(*boy_points, sep='\n')


if __name__ == '__main__':
    main()
