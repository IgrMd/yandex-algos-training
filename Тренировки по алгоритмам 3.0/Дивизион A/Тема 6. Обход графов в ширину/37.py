from collections import deque

rules = {lambda x: x + 1000 if x < 9000 else x,
         lambda x: x - 1 if x % 10 > 1 else x,
         lambda x: x % 1000 * 10 + x // 1000,
         lambda x: x // 10 + x % 10 * 1000}


def read_input():
    start, end = int(input()), int(input())
    return start, end


def bfs(start, end):
    visited = [0] * 10000
    prevs = [-1] * 10000
    queue = deque()
    queue.append(start)
    while len(queue):
        now = queue.popleft()
        distance = visited[now] + 1
        for rule in rules:
            v = rule(now)
            if v == now:
                continue
            if not visited[v] or (visited[v] and distance < visited[v]):
                visited[v] = distance
                prevs[v] = now
                queue.append(v)
    answer = [end]
    prev = prevs[end]
    while prev != start:
        answer.append(prev)
        prev = prevs[prev]
    answer.append(start)
    return answer[::-1]


def main():
    print(*bfs(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
