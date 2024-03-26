def read_input():
    points = []
    w, h, n = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    # with open('input.txt', 'r') as f:
    #     w, h, n = map(int, f.readline().split())
    #     for _ in range(n):
    #         x, y = map(int, f.readline().split())
    #         points.append(Point(x, y))
    return w, h, n, points


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f'[{self.x}, {self.y}]'


class MinMax:
    def __init__(self, min_=0, max_=0):
        self.min = min_
        self.max = max_

    def __repr__(self):
        return f'[{self.min}, {self.max}]'


def check(w, points: list[Point], prefixes: list[MinMax], suffixes: list[MinMax]):
    j = 0
    for i in range(len(points)):
        while j < len(points) and (points[j].x - points[i].x + 1 <= w):
            j += 1
        if i == 0:
            y_min = suffixes[j].min
            y_max = suffixes[j].max
        elif j >= len(points):
            y_min = prefixes[i - 1].min
            y_max = prefixes[i - 1].max
        else:
            y_min = min(prefixes[i - 1].min, suffixes[j].min)
            y_max = max(prefixes[i - 1].max, suffixes[j].max)
        if y_max - y_min + 1 <= w:
            return True
    return False


def upper_bound(l, r, cmp, params):
    while l < r:
        mid = (l + r) // 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid + 1
    return l


def bike_paths(w, h, n, points: list[Point]):
    points.sort()
    prefixes = [MinMax() for _ in range(n)]
    suffixes = [MinMax() for _ in range(n)]
    prefixes[0].min = prefixes[0].max = points[0].y
    suffixes[-1].min = suffixes[-1].max = points[-1].y
    for i in range(1, n):
        prefixes[i].min = min(prefixes[i - 1].min, points[i].y)
        prefixes[i].max = max(prefixes[i - 1].max, points[i].y)
    for i in range(n - 2, -1, -1):
        suffixes[i].min = min(suffixes[i + 1].min, points[i].y)
        suffixes[i].max = max(suffixes[i + 1].max, points[i].y)
    ans = upper_bound(1, min(w, h), check, (points, prefixes, suffixes))
    return ans


if __name__ == '__main__':
    print(bike_paths(*read_input()))
