START = 2
END = 0
WORKER = 1


def bonuses_from_boss(n: int, a: list[int]):
    events = []
    for i, days in enumerate(a):
        events.append((i, WORKER))
        if days < 2:
            continue
        events.append((i, START))
        events.append((i + days, END))
    events.sort()
    bonuses = [0] * n
    cur_workers = 0
    for i, event in events:
        if event == START:
            cur_workers += 1
        elif event == END:
            cur_workers -= 1
        elif event == WORKER:
            bonuses[i] = cur_workers * a[i]
    return sum(bonuses)


def main():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')
    n = int(input().strip())
    a = list(map(int, input().split()))
    print(bonuses_from_boss(n, a))


if __name__ == '__main__':
    main()
