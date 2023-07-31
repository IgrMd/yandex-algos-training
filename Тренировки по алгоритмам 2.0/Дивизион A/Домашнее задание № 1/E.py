def read_input():
    p = int(input())
    return p


def min_max_triangle(p: int):
    a1 = p // 3
    b1 = (p - a1) // 2
    c1 = p - a1 - b1
    if (a1 + b1) <= c1:
        return -1
    a2 = 1 if p % 2 != 0 else 2
    b2 = (p - a2) // 2
    c2 = p - a2 - b2
    return ' '.join(map(str, (a1, b1, c1))) + '\n' + ' '.join(map(str, (a2, b2, c2)))


def main():
    print(min_max_triangle(read_input()))


if __name__ == '__main__':
    main()
