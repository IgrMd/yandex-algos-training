def read_input():
    k = int(input())
    return k


def get_min_rect_coords(k):
    x1, y1 = [int(j) for j in input().split()]
    x2, y2 = x1, y1
    for i in range(1, k):
        x, y = [int(j) for j in input().split()]
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)
    return x1, y1, x2, y2


def main():
    print(*get_min_rect_coords(read_input()))


if __name__ == '__main__':
    main()
