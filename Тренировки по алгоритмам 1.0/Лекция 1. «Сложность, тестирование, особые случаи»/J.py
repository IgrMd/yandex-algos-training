def solve(a, b, c, d, e, f):
    if a == b == c == d == 0:
        if e == f == 0:
            return 5,
        else:
            return 0,

    if a == c == 0:
        if b == 0:
            if e != 0:
                return 0,
            return 4, f / d
        if d == 0:
            if f != 0:
                return 5,
            return 4, e / b
        if e / b != f / d:
            return 0,
        return 4, e / b

    if b == d == 0:
        if a == 0:
            if e != 0:
                return 0,
            return 3, f / c
        if c == 0:
            if f != 0:
                return 0,
            return 3, e / a
        if e / a != f / c:
            return 0,
        return 3, e / a

    if a == b == 0:
        if e != 0:
            return 0,
        return 1, -c / d, f / d

    if c == d == 0:
        if f != 0:
            return 0,
        return 1, -a / b, e / b

    if a == 0:
        return 2, (f - d * e / b) / c, e / b
    if b == 0:
        return 2, e / a, (f - c * e / a) / d
    if c == 0:
        return 2, (e - b * f / d) / a, f / d
    if d == 0:
        return 2, f / c, (e - a * f / c) / a

    if a / c == b / d:
        if e == f == 0:
            return 1, -a / b, 0
        if e == 0 or f == 0:
            return 0,
        if a / c != e / f:
            return 0,
        else:
            return 1, -a / b, e / b

    delta = a * d - c * b
    if delta == 0:
        return 0,
    x = (e * d - f * b) / delta
    y = (f * a - e * c) / delta
    return 2, x, y


assert solve(0, 0, 8, 4, 1, 5) == (0,)
assert solve(1, 2, 3, 4, 5, 6) == (2, -4, 4.5)

assert solve(1, 1, 2, 2, 0, 1) == (0,)
assert solve(1, 1, 2, 2, 0, 0) == (1, -1, 0)

assert solve(0, 0, 0, 0, 0, 0) == (5,)
assert solve(0, 0, 0, 0, 1, 0) == (0,)
assert solve(0, 0, 0, 2, 0, 5) == (4, 2.5)

assert solve(0, 2, 0, 4, 1, 2) == (4, 0.5)
assert solve(2, 0, 4, 0, 1, 2) == (3, 0.5)
assert solve(1, 0, 0, 1, 3, 3) == (2, 3, 3)
assert solve(0, 1, 1, 0, 3, 3) == (2, 3, 3)

assert solve(3, 4, 3, 4, 12, 18) == (0,)
assert solve(1, 1, 2, 2, 5, 7) == (0,)

assert solve(1, 1, 2, 2, 1, 2) == (1, -1, 1)
assert solve(0, 2, 0, 4, 1, 2) == (4, 0.5)

assert solve(1, 0, 0, 1, 3, 3) == (2, 3.00000, 3.00000)
assert solve(2, 2, 3, -3, 6, -3) == (2, 1.00000, 2.00000)
assert solve(1, 1, 1, -1, 3, -1) == (2, 1.00000, 2.00000)
assert solve(1, 1, 2, 2, 1, 2) == (1, -1.00000, 1.00000)
assert solve(1, 1, 1, 1, 1, 2) == (0,)
assert solve(0, 1, 0, 1, 2, 3) == (0,)
assert solve(0, 1, 0, 2, 2, 4) == (4, 2.00000)
assert solve(1, 0, 2, 0, 2, 4) == (3, 2.00000)
assert solve(0, 0, 0, 0, 0, 0) == (5,)
assert solve(0, 0, 0, 0, 1, 0) == (0,)
assert solve(0, 2, 0, 4, 1, 2) == (4, 0.50000)
assert solve(0, 2, 0, 4, 1, 2) == (4, 0.50000)
assert solve(0, 0, 2, 4, 0, 2) == (1, -0.50000, 0.50000)
assert solve(2, 4, 0, 0, 2, 0) == (1, -0.50000, 0.50000)
assert solve(2, 0, 3, 0, 2, 3) == (3, 1.00000)
assert solve(2, 2, 3, 0, 6, 3) == (2, 1.00000, 2.00000)
assert solve(1, 1, 1.5, 0, 3, 1.5) == (2, 1.00000, 2.00000)


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    print(*solve(a, b, c, d, e, f))


if __name__ == '__main__':
    main()
