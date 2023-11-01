import math


def read_input():
    x_a, y_a, x_b, y_b = [int(x) for x in input().strip().split()]
    return x_a, y_a, x_b, y_b


def min_dist(x_a, y_a, x_b, y_b):
    r1 = math.sqrt(x_a * x_a + y_a * y_a)
    r2 = math.sqrt(x_b * x_b + y_b * y_b)
    if r1 * r2 == 0.:
        return r1 + r2
    alpha1 = math.atan(abs(y_a / x_a)) if x_a != 0 else math.pi / 2
    alpha2 = math.atan(abs(y_b / x_b)) if x_b != 0 else math.pi / 2
    if x_a < 0:
        alpha1 = math.pi - alpha1
    if y_a < 0:
        alpha1 *= -1
    if x_b < 0:
        alpha2 = math.pi - alpha2
    if y_b < 0:
        alpha2 *= -1
    alpha = abs(alpha1 - alpha2)
    path1 = r1 + r2
    path2 = min(r1, r2) * alpha + abs(r1 - r2)
    return min(path1, path2)


def main():
    print(min_dist(*read_input()))


if __name__ == '__main__':
    main()
