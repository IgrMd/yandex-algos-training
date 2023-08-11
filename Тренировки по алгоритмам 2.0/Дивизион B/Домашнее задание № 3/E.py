def read_input():
    m = int(input())
    witnesses = [set(input().strip()) for _ in range(m)]
    n = int(input())
    cars = []
    for _ in range(n):
        car = input().strip()
        cars.append([car, set(car), 0])
    return m, witnesses, n, cars


def cars_nums(m: int, witnesses: list[set], n: int, cars: list[(set, int)]):
    best_count = 0
    for witness in witnesses:
        for car in cars:
            if witness.issubset(car[1]):
                car[2] += 1
                best_count = max(best_count, car[2])
    return [car[0] for car in cars if car[2] == best_count]


def main():
    print(*cars_nums(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
