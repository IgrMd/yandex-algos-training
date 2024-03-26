from dataclasses import dataclass


def read_input():
    d, n = map(int, input().split())
    players = [Player(*map(int, input().split())) for _ in range(n)]
    return d, n, players


@dataclass
class Point:
    x: int
    y: int

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Circle:
    p: Point
    r: float

    def is_p_inside(self, p: Point):
        return ((p.x - self.p.x) * (p.x - self.p.x) + (p.y - self.p.y) * (p.y - self.p.y)) < self.r * self.r

    def __init__(self, x, y, r):
        self.p = Point(x, y)
        self.r = r

    def __repr__(self):
        return f'({self.p.x}, {self.p.y}, {self.r})'


class Player:
    p: Point
    v: int

    def __init__(self, x, y, v):
        self.p = Point(x, y)
        self.v = v

    def __repr__(self):
        return f'({self.p.x}, {self.p.y}, {self.v})'


def find_intersection(c1: Circle, c2: Circle):
    d2 = (c1.p.x - c2.p.x) ** 2 + (c1.p.y - c2.p.y) ** 2
    d = d2 ** 0.5
    if d > c1.r + c2.r or d < abs(c1.r - c2.r):
        return []
    a = (c1.r * c1.r - c2.r * c2.r + d2) / (2 * d)
    h = (c1.r * c1.r - a * a) ** 0.5
    p2 = c1.p + (c2.p - c1.p) / d * a
    x1 = p2.x + h * (c1.p.y - c2.p.y) / d
    x2 = p2.x - h * (c1.p.y - c2.p.y) / d
    y1 = p2.y - h * (c1.p.x - c2.p.x) / d
    y2 = p2.y + h * (c1.p.x - c2.p.x) / d
    return [Point(x1, y1), Point(x2, y2)]


def is_good_point(point: Point, d):
    return point.y >= 0 and (point.x * point.x + point.y * point.y <= d * d)


def upper_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    if not cmp(l, *params):
        l += 1
    return l


def lower_bound_f(l, r, eps, cmp, params):
    while abs(r - l) >= eps:
        mid = (l + r) / 2
        if cmp(mid, *params):
            l = mid
        else:
            r = mid
    # if not cmp(l, *params):
    #     l -= EPS
    return l


def circles_intersect_line(c: Circle, y: int):
    if c.p.y + c.r <= y or y <= c.p.y - c.r:
        return None
    dy = y - c.p.y
    dx = (c.r * c.r - dy * dy) ** 0.5
    return [Point(c.p.x + dx, y), Point(c.p.x - dx, y)]


def check_time(t, d, n, players: list[Player]):
    circles = []
    p1, p2, p3 = Point(-d, 0), Point(d, 0), Point(0, d)
    for player in players:
        circles.append(Circle(player.p.x, player.p.y, player.v * t))
        if circles[-1].is_p_inside(p1) and circles[-1].is_p_inside(p2) and circles[-1].is_p_inside(p3):
            return False
    circles.append(Circle(0, 0, d))
    points = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            c1 = circles[i]
            c2 = circles[j]
            buf = find_intersection(c1, c2)
            for point in buf:
                if j == n:
                    if point.y >= 0:
                        points.append((point, i, j))
                elif is_good_point(point, d):
                    points.append((point, i, j))
    if not len(points):
        all_inside = True
        all_outside = True
        for i in range(n):
            c = circles[i]
            dist = (c.p.x * c.p.x + c.p.y * c.p.y) ** 0.5
            all_inside = dist + c.r < d
            all_outside = dist > d + c.r
        if all_inside:
            return True
        if all_outside:
            return True
        return False
    for point, i, j in points:
        flag = False
        for k in range(n):
            if k == i or k == j:
                continue
            flag = flag or circles[k].is_p_inside(point)
        if not flag:
            return True
    return False


def find_max_time(d, players: list[Player]):
    ans = 0
    for player in players:
        t = ((player.p.x * player.p.x + player.p.y * player.p.y) ** 0.5 + d) / player.v
        ans = max(ans, t)
    return ans + EPS


EPS = 1e-9


def strike(d, n, players: list[Player]):
    max_time = find_max_time(d, players)
    t = lower_bound_f(0, max_time, EPS, check_time, (d, n, players))

    circles = []
    for player in players:
        circles.append(Circle(player.p.x, player.p.y, player.v * t))
    circles.append(Circle(0, 0, d))
    points = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            c1 = circles[i]
            c2 = circles[j]
            buf = find_intersection(c1, c2)
            for point in buf:
                if j == n:
                    if point.y >= 0:
                        points.append((point, i, j))
                elif is_good_point(point, d):
                    points.append((point, i, j))
    for i in range(n):
        if buf := circles_intersect_line(circles[i], 0):
            points.extend(buf)
    for point, i, j in points:
        flag = False
        for k in range(n):
            if k == i or k == j:
                continue
            flag = flag or circles[k].is_p_inside(point)
        if not flag:
            break

    return t, point


# find_intersection(Circle(1, 1, 3), Circle(3, 1, 2))
# find_intersection(Circle(1, 1, 1), Circle(2, 2, 1))
# find_intersection(Circle(1, 1, 1), Circle(1, 3, 1))

if __name__ == '__main__':
    t, point = strike(*read_input())
    print(t)
    print(point.x, point.y)
