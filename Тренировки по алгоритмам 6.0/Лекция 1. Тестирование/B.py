def read_input():
    a, b, c, d = [int(input()) for _ in range(4)]
    return a, b, c, d


def wardrobe(a, b, c, d):
    if a == 0:
        return 1, c + 1 if c != 0 else 1
    if b == 0:
        return 1, d + 1 if d != 0 else 1
    if c == 0:
        return a + 1 if a != 0 else 1, 1
    if d == 0:
        return b + 1 if b != 0 else 1, 1

    variants = []
    variants.append((1, max(c, d) + 1))
    variants.append((max(a, b) + 1, 1))
    variants.append((a + 1, c + 1))
    variants.append((b + 1, d + 1))

    res = min(variants, key=lambda x: sum(x))
    return res


assert (wardrobe(15, 0, 555, 0) == (1, 1))
assert (wardrobe(11, 1111, 111, 0) == (1112, 1))
assert (wardrobe(13, 6666, 0, 11) == (14, 1))
assert (wardrobe(6, 2, 7, 3) == (3, 4))
assert (wardrobe(0, 1, 0, 1) == (1, 1))
assert (wardrobe(1, 0, 1, 0) == (1, 1))
assert (wardrobe(1, 0, 1, 1) == (1, 2))

assert (wardrobe(0, 2, 5, 1) == (1, 6))


assert (wardrobe(1, 1, 66, 1) == (2, 1))
assert (wardrobe(42, 2, 1, 1) == (1, 2))

assert (wardrobe(1, 1, 1, 1) == (2, 1) or wardrobe(1, 1, 1, 1) == (1, 2))


def main():
    print(*wardrobe(*read_input()))


if __name__ == '__main__':
    main()
