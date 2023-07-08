from heapq import heappush, heappushpop


class Task:
    def __init__(self, s, i):
        self.a, self.T = [int(x) for x in s.split()]
        self.i = i
        self.worker = -1

    def __eq__(self, other):
        return (self.a, self.T) == (other.a, other.T)

    def __lt__(self, other):
        return self.a + self.T < other.a + other.T

    def __str__(self):
        return str(self.i)


def read_input():
    n, w = [int(x) for x in input().split()]
    tasks = []
    for i in range(n):
        tasks.append(Task(input(), i + 1))
    tasks.sort(key=lambda task: task.a)
    return n, w, tasks


def workers_tasks(n, w, tasks: list[Task]):
    tasks[0].worker = 0
    workers = [[tasks[0]]]
    task_queue = []
    heappush(task_queue, tasks[0])
    for i in range(1, n):
        now = tasks[i]
        last = task_queue[0]
        if last.a + last.T <= now.a:
            now.worker = last.worker
            workers[now.worker].append(now)
            heappushpop(task_queue, now)
            continue
        now.worker = len(workers)
        workers.append([now])
        heappush(task_queue, now)

    print(len(workers))
    for worker in workers:
        print(*worker, end=' ')


def main():
    workers_tasks(*read_input())


if __name__ == '__main__':
    main()
