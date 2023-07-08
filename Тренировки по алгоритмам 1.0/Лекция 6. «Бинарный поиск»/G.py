def read_input():
    n = int(input())
    m = int(input())
    t = int(input())
    return n, m, t


def upper_bound(left: int, right: int, check_func, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check_func(mid, params):
            left = mid
        else:
            right = mid - 1
    return left


def check_road_width(width, params):
    n, m, t = params
    tile_count = 2 * width * n + 2 * width * m - 4 * width * width
    return tile_count <= t


def max_road_width(n, m, t):
    max_width = min(n, m) // 2
    width = upper_bound(0, max_width, check_road_width, (n, m, t))
    return width


def main():
    print(max_road_width(*read_input()))


if __name__ == '__main__':
    main()
