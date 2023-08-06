from math import ceil, floor


def read_input():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    x3, y3, r = [int(x) for x in input().split()]
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    return x1, y1, x2, y2, x3, y3, r


def seg_coords_circle_intersect(y, xc, yc, r):
    dx = (r ** 2 - (y - yc) ** 2) ** 0.5
    xl = ceil(xc - dx)
    xr = floor(xc + dx)
    return xl, xr


def segs_cross_points(seg1_x1, seg1_x2, seg2_x1, seg2_x2):
    x1 = max(seg1_x1, seg2_x1)
    x2 = min(seg1_x2, seg2_x2)
    if x1 > x2:
        return 0
    return x2 - x1 + 1


def grass(x1, y1, x2, y2, x3, y3, r):
    grass_cut = 0
    for y in range(max(y1, y3 - r), min(y2, y3 + r) + 1):
        circle_l, circle_r = seg_coords_circle_intersect(y, x3, y3, r)
        grass_cut += segs_cross_points(circle_l, circle_r, x1, x2)
    return grass_cut


def main():
    print(grass(*read_input()))


if __name__ == '__main__':
    main()
