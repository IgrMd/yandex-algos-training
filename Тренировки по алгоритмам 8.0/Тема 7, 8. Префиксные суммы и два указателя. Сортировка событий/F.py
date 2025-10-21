import sys

START = 0
END = 1
CAR = 2


def railway_crossing(n, m, x, trains, cars):
    events = []
    for a, b, v in trains:
        if a < b:
            events.append(((x - a) / v, END))
            events.append(((x - b) / v, START))
        else:
            events.append(((a - x) / v, END))
            events.append(((b - x) / v, START))

    for i, car in enumerate(cars):
        events.append((car, CAR, i))
    events.sort()
    cur_cars = []
    cur_trains = 0
    ans = []
    for event in events:
        if event[1] == START:
            cur_trains += 1
        elif event[1] == CAR:
            cur_cars.append(event[2])
        elif event[1] == END:
            cur_trains -= 1
        while cur_trains == 0 and cur_cars:
            ans.append((cur_cars.pop(), event[0]))
    ans.sort()
    return map(lambda e: e[1], ans)


def main():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')
    n, m, x = map(int, input().split())
    trains = []
    for _ in range(n):
        a, b, v = map(int, input().split())
        trains.append((a, b, v))
    cars = list(map(int, input().split()))
    print(*railway_crossing(n, m, x, trains, cars), sep='\n')


if __name__ == '__main__':
    main()
