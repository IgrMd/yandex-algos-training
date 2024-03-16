from collections import defaultdict


def read_input():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return n, points


def square(n, points: list):
    init_x, init_y = points[0]
    ans = [(init_x + 1, init_y), (init_x, init_y + 1), (init_x + 1, init_y + 1)]
    if n == 1:
        return ans
    y_to_xs = defaultdict(set)
    for x, y in points:
        y_to_xs[y].add(x)
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                continue
            xa, ya = points[i]
            xb, yb = points[j]
            dx = xb - xa
            dy = yb - ya
            if yb - dx in y_to_xs and xb + dy in y_to_xs[yb - dx]:
                if ya - dx in y_to_xs and xa + dy in y_to_xs[ya - dx]:
                    return []
                if len(ans) > 1:
                    ans.clear()
                    ans.append((xa + dy, ya - dx))
            elif ya - dx in y_to_xs and xa + dy in y_to_xs[ya - dx]:
                if len(ans) > 1:
                    ans.clear()
                    ans.append((xb + dy, yb - dx))
            if yb + dx in y_to_xs and xb - dy in y_to_xs[yb + dx]:
                if ya + dx in y_to_xs and xa - dy in y_to_xs[ya + dx]:
                    return []
                if len(ans) > 1:
                    ans.clear()
                    ans.append((xa - dy, ya + dx))
            elif ya + dx in y_to_xs and xa - dy in y_to_xs[ya + dx]:
                if len(ans) > 1:
                    ans.clear()
                    ans.append((xb - dy, yb + dx))
            if len(ans) > 2:
                ans.clear()
                ans.append((xa + dy, ya - dx))
                ans.append((xb + dy, yb - dx))
    return ans


def main():
    ans = square(*read_input())
    print(len(ans))
    for poit in ans:
        print(*poit, sep=' ')


if __name__ == '__main__':
    main()
