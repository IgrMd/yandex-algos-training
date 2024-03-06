def read_input():
    k = int(input())
    points = []
    for _ in range(k):
        x, y = map(int, input().split())
        points.append((x, y))
    return k, points


def min_rectangle(k, points):
    xl, yl, xr, yr = points[0][0], points[0][1], points[0][0], points[0][1]
    for x, y in points:
        xl = min(xl, x)
        yl = min(yl, y)
        xr = max(xr, x)
        yr = max(yr, y)
    return xl, yl, xr, yr


def main():
    print(*min_rectangle(*read_input()), sep=' ')


if __name__ == '__main__':
    main()
