def read_input():
    test = [int(x) for x in input().split()]
    return test


def check_guards(n: int, events: list):
    if events[0][0] != 0 or events[-1][0] != 10000:
        return False
    good_guards = set()
    now_guards = set()
    last_event_time = -1
    for event in events:
        if event[0] != 0 and len(now_guards) == 0:
            return False
        if len(now_guards) == 1 and last_event_time != event[0]:
            good_guards.update(now_guards)
        if event[1] == 1:
            now_guards.remove(event[2])
        if event[1] == 0:
            now_guards.add(event[2])
        last_event_time = event[0]
    return len(good_guards) == n


def guards():
    for _ in range(int(input())):
        test = read_input()
        n = test[0]
        events = []
        for i in range(1, len(test)):
            if i % 2 == 0:  # Left
                events.append((test[i], 1, (i - 1) // 2))
            else:  # Come
                events.append((test[i], 0, (i - 1) // 2))
        events.sort()
        if check_guards(n, events):
            print('Accepted')
        else:
            print('Wrong Answer')


def main():
    guards()


if __name__ == '__main__':
    main()
