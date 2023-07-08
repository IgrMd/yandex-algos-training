def to_minutes(s: str) -> int:
    result = s.split(sep=':')
    result = int(result[0]) * 60 + int(result[1])
    return result


def read_input():
    n, m = [int(x) for x in input().split()]
    routes = []
    for _ in range(m):
        start_town, start_t, end_town, end_t = input().split()
        start_town, end_town = int(start_town), int(end_town)
        start_t = to_minutes(start_t)
        end_t = to_minutes(end_t)
        routes.append((start_town, start_t, end_town, end_t))
    return n, m, routes


def busses(n, m, routes):
    events = []
    balances = [0] * (n + 1)
    night_buses = 0
    for start_town, start_t, end_town, end_t in routes:
        balances[start_town] -= 1
        balances[end_town] += 1
        if start_t > end_t:
            night_buses += 1
        events.append((start_t, 1, start_town))
        events.append((end_t, 0, end_town))

    for balance in balances:
        if balance != 0:
            return -1

    events.sort()
    buses_count = [0] * (n + 1)
    for time, action, town in events:
        if action == 0:
            buses_count[town] += 1
        if action == 1:
            if buses_count[town] > 0:
                buses_count[town] -= 1
    return night_buses + sum(buses_count)


def main():
    print(busses(*read_input()))


if __name__ == '__main__':
    main()
