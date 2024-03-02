def read_input():
    p, v = [int(x) for x in input().split()]
    q, m = [int(x) for x in input().split()]
    return p, v, q, m


def paint_tries(p, v, q, m):
    intrval1 = [p - v, p + v]
    intrval2 = [q - m, q + m]
    if (intrval2[0] <= intrval1[0] <= intrval2[1]) or (intrval1[0] <= intrval2[0] <= intrval1[1]):
        return max(intrval1[1], intrval2[1]) - min(intrval1[0], intrval2[0]) + 1
    else:
        return intrval1[1] - intrval1[0] + intrval2[1] - intrval2[0] + 2


def main():
    print(paint_tries(*read_input()))


if __name__ == '__main__':
    main()
