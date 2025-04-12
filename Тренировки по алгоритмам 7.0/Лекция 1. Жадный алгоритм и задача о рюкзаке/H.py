from heapq import heappush, heappop


def read_input():
    n = int(input().strip())
    tasks = [input().strip() for _ in range(n)]
    return n, tasks


def task_distribution(n: int, tasks: list[str]):
    odds = []
    even_buf1, even_buf2 = 0, 0
    for i, task in enumerate(tasks):
        even_count, odd_count = 0, 0
        for j in range(0, len(task), 2):
            even_count += task[j] == 'S'
        for j in range(1, len(task), 2):
            odd_count += task[j] == 'S'
        if len(task) % 2:
            odds.append((even_count, odd_count))
        else:
            even_buf1 += even_count
            even_buf2 += max(even_count, odd_count)
    ans = even_buf2 if odds else even_buf1

    odds.sort(key=lambda x: x[0] - x[1], reverse=True)
    mid = (len(odds) - 1) // 2
    for i in range(len(odds)):
        if i <= mid:
            ans += odds[i][0]
        else:
            ans += odds[i][1]
    return ans


def main():
    print(task_distribution(*read_input()))


if __name__ == '__main__':
    main()
