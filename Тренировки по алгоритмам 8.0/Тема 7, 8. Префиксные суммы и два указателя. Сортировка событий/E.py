START = 0
END = 2
HOLE = 1


def pothole_repair(n, m, k, holes, routes):
    events = []
    for l, r in routes:
        events.append((l, START))
        events.append((r, END))
    for i, hole in enumerate(holes):
        events.append((i, HOLE, hole))
    holes_and_routes = []
    events.sort()
    curr_routes = 0
    for event in events:
        if event[1] == HOLE:
            holes_and_routes.append((curr_routes, event[2]))
        elif event[1] == START:
            curr_routes += 1
        elif event[1] == END:
            curr_routes -= 1
    holes_and_routes.sort(reverse=True)
    start = n
    for i in range(n):
        if k > holes_and_routes[i][1]:
            k -= holes_and_routes[i][1]
        else:
            r, h = holes_and_routes[i][0], holes_and_routes[i][1] - k
            holes_and_routes[i] = r, h
            start = i
            break
    ans = 0
    for j in range(start, n):
        ans += holes_and_routes[j][0] * holes_and_routes[j][1]
    return ans


def main():
    n, m, k = map(int, input().split())
    holes = list(map(int, input().split()))
    routes = []
    for _ in range(m):
        l, r = map(int, input().split())
        routes.append((l - 1, r - 1))
    print(pothole_repair(n, m, k, holes, routes))


if __name__ == '__main__':
    main()
