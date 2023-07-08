def read_input():
    n = int(input())
    turtles = [[int(x) for x in input().split()] for _ in range(n)]
    return n, turtles


def truthful_turtles(n, turtles):
    good_turtles = set()
    for before, after in turtles:
        if before < 0 or after < 0:
            continue
        if before + after + 1 == n:
            good_turtles.add(before + 1)
    return len(good_turtles)


def main():
    print(truthful_turtles(*read_input()))


if __name__ == '__main__':
    main()
