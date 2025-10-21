def transport_taxes(n, m, table, cars):
    sorted_cars = []
    for i, car in enumerate(cars):
        sorted_cars.append((car, i))
    sorted_cars.sort()
    ans = []
    r = 0
    for l in range(m):
        car, i = sorted_cars[l]
        while r < n and table[r][0] < car:
            r += 1
        if table[r - 1][0] < car:
            r -= 1
        if r == n:
            tax = car * table[-1][1]
        else:
            tax = car * table[r][1]
        ans.append((i, tax))
    ans.sort()
    print(*map(lambda x: x[1], ans), sep='\n')


def main():
    n = int(input().strip())
    table = [list(map(int, input().split())) for _ in range(n)]
    m = int(input().strip())
    cars = [int(input().strip()) for _ in range(m)]
    transport_taxes(n, m, table, cars)


if __name__ == '__main__':
    main()
