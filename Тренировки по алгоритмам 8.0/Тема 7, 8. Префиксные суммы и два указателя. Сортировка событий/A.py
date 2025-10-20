def read_input():
    busses = []
    n = int(input().strip())
    for _ in range(n):
        bus = input().strip().split(sep='-')
        busses.append((bus[0], START, 1))
        busses.append((bus[1], STOP, 1))
    m = int(input().strip())
    for _ in range(m):
        bus = input().strip().split(sep='-')
        busses.append((bus[0], START, 2))
        busses.append((bus[1], STOP, 2))
    return n, m, busses


START = 1
STOP = 0


def routes_between_offices(n: int, m: int, busses: list):
    busses.sort()
    ans = 0
    at_1st_stop, at_2nd_stop = 0, 0
    at_1st_route, at_2nd_route = 0, 0
    for _, event, route in busses:
        if event == START:
            if route == 1:
                at_1st_stop = max(0, at_1st_stop - 1)
                at_1st_route += 1
            if route == 2:
                at_2nd_stop = max(0, at_2nd_stop - 1)
                at_2nd_route += 1
        if event == STOP:
            if route == 1:
                at_2nd_stop += 1
                at_1st_route -= 1
            if route == 2:
                at_1st_stop += 1
                at_2nd_route -= 1
        ans = max(ans, at_1st_stop + at_2nd_stop + at_1st_route + at_2nd_route)
    return ans


def main():
    print(routes_between_offices(*read_input()))


if __name__ == '__main__':
    main()
