def read_input():
    n = int(input())
    schedule = [[int(x) for x in input().split()] for _ in range(n)]
    return n, schedule


def time_all_cashes_open(n: int, schedule: list, ):
    events = []
    for open_h, open_m, close_h, close_m in schedule:
        open_t = open_h * 60 + open_m
        close_t = close_h * 60 + close_m
        if (open_h, open_m) < (close_h, close_m):
            events.append((open_t, 1))
            events.append((close_t, -1))
        else:
            open_midnight = 0
            close_midnight = 24 * 60
            events.append((open_t, 1))
            events.append((close_midnight, -1))
            events.append((open_midnight, 1))
            events.append((close_t, -1))
    events.sort()
    curr_cashes_open = 0
    all_cashes_open_t = 0
    for i, event in enumerate(events):
        match event[1]:
            case -1:
                if curr_cashes_open == n:
                    all_cashes_open_t += event[0] - events[i - 1][0]
                curr_cashes_open -= 1
            case 1:
                curr_cashes_open += 1
    return all_cashes_open_t


def main():
    print(time_all_cashes_open(*read_input()))


if __name__ == '__main__':
    main()
