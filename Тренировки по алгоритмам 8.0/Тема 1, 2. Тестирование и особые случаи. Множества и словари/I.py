def read_input():
    x, y = map(int, input().split())
    f, g = map(int, input().split())
    return x, y, f, g


def new_rules(x, y, f, g):
    dx = abs(x - f)
    dy = abs(y - g)
    ans = 0
    ans += max(0, dx - 1) * 3
    ans += max(0, dy - 1) * 3
    if dx > 0 and dy > 0:
        ans += 1
    return ans


def main():
    print(new_rules(*read_input()))


if __name__ == '__main__':
    main()
