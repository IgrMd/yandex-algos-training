from dataclasses import dataclass
from enum import Enum


def read_input():
    n, h = input().split()
    n, h = int(n), float(h)
    points = [Point(*map(int, input().split()), Type.OTHER) for _ in range(n + 1)]
    return n, h, points


MAX_LEVEL = 10 ** 12
MIN_LEVEL = -10 ** 12
EPS = 1e-6


class Type(Enum):
    OTHER = 0
    PEAK = 1
    DEEP = 2
    LEFT_WALL = 3
    RIGHT_WALL = 4


@dataclass
class Point:
    x: int
    y: int
    type: Type


def upper_bound_f(l, r, eps, cmp, params):
    while abs(r - l) >= eps:
        mid = (l + r) / 2
        if cmp(mid, *params):
            r = mid
        else:
            l = mid
    return l


def lower_bound_f(l, r, eps, cmp, params):
    while abs(r - l) >= eps:
        mid = (l + r) / 2
        if cmp(mid, *params):
            l = mid
        else:
            r = mid
    return l


def highest_mid_peak(l, r, points: list[Point]):
    ans = None
    max_y = MIN_LEVEL
    for i in range(l + 1, r):
        if points[i].type == Type.PEAK and points[i].y > max_y:
            ans = i
            max_y = points[i].y
    return ans


def calc_value(p1: Point, p2: Point, h):
    if h <= min(p1.y, p2.y):
        return 0
    dx = abs(p2.x - p1.x)
    dy = abs(p2.y - p1.y)
    s = dx * dy / 2
    if h >= max(p1.y, p2.y):
        ans = s + dx * (h - max(p1.y, p2.y))
    else:
        k = (h - min(p1.y, p2.y)) / dy
        ans = s * k * k
    return ans


def capacity(l, r, points: list[Point]):
    h = min_peak_of_two(l, r, points)
    cap = 0
    for i in range(l, r):
        cap += calc_value(points[i], points[i + 1], h)
    return cap


def min_peak_of_two(l, r, points: list[Point]):
    if points[l].type == Type.LEFT_WALL and points[r].type == Type.RIGHT_WALL:
        return MAX_LEVEL
    elif points[l].type == Type.LEFT_WALL:
        return points[r].y
    elif points[r].type == Type.RIGHT_WALL:
        return points[l].y
    return min(points[l].y, points[r].y)


def try_accommodate(l, r, value, points: list[Point]):
    if points[l].type == Type.LEFT_WALL and points[r].type == Type.RIGHT_WALL:
        return True, 10 ** 10
    cap = capacity(l, r, points)
    return cap >= value, cap


def check_h(h, l, r, target_v, points: list[Point]):
    v = 0
    for i in range(l, r):
        v += calc_value(points[i], points[i + 1], h)
    return v > target_v


def calc_h(l, r, target_v, points: list[Point]):
    min_level = MAX_LEVEL
    for i in range(l, r + 1):
        min_level = min(min_level, points[i].y)
    max_level = min_peak_of_two(l, r, points)
    h = upper_bound_f(min_level, max_level, EPS, check_h, (l, r, target_v, points))
    return h


def fill_exact(l, r, h, water_levels: list[int]):
    while l <= r:
        water_levels[l] = max(h, water_levels[l])
        l += 1


def fill_levels(l, r, v, points: list[Point], water_levels: list[int], extra_left, extra_right):
    mid_peak = highest_mid_peak(l, r, points)
    if not mid_peak:
        v1 = v + extra_left + extra_right
        local_h = calc_h(l, r, v1, points)
        fill_exact(l, r, local_h, water_levels)
        return
    left_v = v * ((points[mid_peak].x - points[l].x) / (points[r].x - points[l].x))
    right_v = v - left_v
    left_ok, left_cap = try_accommodate(l, mid_peak, left_v + extra_left, points)
    right_ok, right_cap = try_accommodate(mid_peak, r, right_v + extra_right, points)
    if left_ok and right_ok:
        fill_levels(l, mid_peak, left_v, points, water_levels, extra_left, 0)
        fill_levels(mid_peak, r, right_v, points, water_levels, 0, extra_right)
        return
    elif left_ok:
        extra_right1 = right_v + extra_right - right_cap
        if left_cap > left_v + extra_left + extra_right1:
            fill_exact(mid_peak, r, min_peak_of_two(mid_peak, r, points), water_levels)
            fill_levels(l, mid_peak, left_v, points, water_levels, extra_left, extra_right1)
            return
    elif right_ok:
        extra_left1 = left_v + extra_left - left_cap
        if right_cap > right_v + extra_left1 + extra_right:
            fill_exact(l, mid_peak, min_peak_of_two(l, mid_peak, points), water_levels)
            fill_levels(mid_peak, r, right_v, points, water_levels, extra_left1, extra_right)
            return
    local_h1 = calc_h(l, r, v + extra_left + extra_right, points)
    fill_exact(l, r, local_h1, water_levels)
    return None


def rain(n, h, points: list[Point]):
    points.sort(key=lambda p: p.x)
    points[0].type = Type.LEFT_WALL
    for i in range(1, n):
        if points[i - 1].y > points[i].y and points[i].y < points[i + 1].y:
            points[i].type = Type.DEEP
        elif points[i - 1].y < points[i].y and points[i].y > points[i + 1].y:
            points[i].type = Type.PEAK
    points[-1].type = Type.RIGHT_WALL
    water_levels = [MIN_LEVEL] * (n + 1)
    fill_levels(0, n, h * (points[-1].x - points[0].x), points, water_levels, 0, 0)
    ans = water_levels[0] - points[0].y
    for i in range(n + 1):
        ans = max(ans, water_levels[i] - points[i].y)
    return ans


if __name__ == '__main__':
    print(rain(*read_input()))
