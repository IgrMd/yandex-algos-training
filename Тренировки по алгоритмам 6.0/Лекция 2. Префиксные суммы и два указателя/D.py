def read_input():
    n, k = map(int, input().split())
    tasks = list(map(int, input().split()))
    return n, k, tasks


def days_to_complete_tasks(n, k, tasks: list[int]):
    cur_day = 0
    tasks.sort()
    days = [0] * n
    r = 0
    for l in range(n):
        if days[l] == 0:
            cur_day += 1
            days[l] = cur_day
        while r < n and (tasks[r] - tasks[l] <= k or days[r] != 0):
            r += 1
        if r < n:
            days[r] = days[l]
    return cur_day


def main():
    print(days_to_complete_tasks(*read_input()))


if __name__ == '__main__':
    main()
