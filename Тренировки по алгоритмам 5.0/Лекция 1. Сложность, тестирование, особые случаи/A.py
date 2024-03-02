def read_input():
    p, v = [int(x) for x in input().split()]
    q, m = [int(x) for x in input().split()]
    return p, v, q, m


def paint_tries(p, v, q, m):
    interval1 = [p - v, p + v]
    interval2 = [q - m, q + m]
    if (interval2[0] <= interval1[0] <= interval2[1]) or (interval1[0] <= interval2[0] <= interval1[1]):
        return max(interval1[1], interval2[1]) - min(interval1[0], interval2[0]) + 1
    else:
        return interval1[1] - interval1[0] + interval2[1] - interval2[0] + 2


def main():
    print(paint_tries(*read_input()))


if __name__ == '__main__':
    main()
