def candidates_queue():
    n, x = map(int, input().split())
    queue = list(map(int, input().split()))
    l, r = 0, 0
    m = int(input().strip())
    prefs = [0] * (n + 1)
    for i in range(n):
        prefs[i + 1] = prefs[i] + int(queue[i] >= x)
    left = 0
    for _ in range(m):
        event = list(map(int, input().split()))
        if len(event) == 1:
            if queue[l] >= x:
                left += 1
            l += 1
        elif event[0] == 1:
            queue.append(event[1])
            prefs.append(prefs[-1] + int(queue[-1] >= x))
        elif event[0] == 3:
            print(prefs[min(len(prefs) - 1, l + event[1])] - left)


if __name__ == '__main__':
    candidates_queue()
