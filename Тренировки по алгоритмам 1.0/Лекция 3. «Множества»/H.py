def read_input():
    n = int(input())
    birds = [[int(x) for x in input().split()] for _ in range(n)]
    return n, birds


def shots_n(n, birds):
    shots = set()
    for x, y in birds:
        shots.add(x)
    return len(shots)


def main():
    print(shots_n(*read_input()))


if __name__ == '__main__':
    main()
