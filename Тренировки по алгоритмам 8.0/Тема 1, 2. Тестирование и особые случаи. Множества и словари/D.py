from collections import defaultdict


def read_input():
    n, k = map(int, input().split())
    tasks = list(map(int, input().split()))
    return n, k, tasks


def contest(n, k, tasks):
    unique_tasks = defaultdict(int)
    for task in tasks:
        unique_tasks[task] += 1
    ans = []
    while True:
        for task in unique_tasks.keys():
            if unique_tasks[task] == 0:
                continue
            ans.append(task)
            unique_tasks[task] -= 1
            if len(ans) == k:
                return ans


def main():
    print(*contest(*read_input()))


if __name__ == '__main__':
    main()
