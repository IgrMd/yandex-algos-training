def read_input():
    n = int(input())
    events = []
    for human_id in range(1, n + 1):
        birth_d, birth_m, birth_y, death_d, death_m, death_y = [int(x) for x in input().split()]
        adult_d, adult_m, adult_y = birth_d, birth_m, birth_y + 18
        if (adult_y, adult_m, adult_d) > (death_y, death_m, death_d):
            continue
        events.append((adult_y, adult_m, adult_d, 1, human_id))
        old_d, old_m, old_y = birth_d, birth_m, birth_y + 80
        if (death_y, death_m, death_d) > (old_y, old_m, old_d):
            events.append((old_y, old_m, old_d, -1, human_id))
        else:
            events.append((death_y, death_m, death_d, -1, human_id))
    return n, events


def coevals(n: int, events: list, ):
    if len(events) == 0:
        print(0)
        return
    curr_coevals = set()
    last_action = 0
    events.sort()
    for i in range(len(events)):
        event = events[i]
        if event[3] == 1:
            last_action = 1
            curr_coevals.add(event[4])
        if event[3] == -1:
            if last_action == 1:
                print(*curr_coevals)
            last_action = -1
            curr_coevals.remove(event[4])


def main():
    coevals(*read_input())


if __name__ == '__main__':
    main()
