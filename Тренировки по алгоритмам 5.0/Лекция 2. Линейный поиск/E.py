def read_input():
    n = int(input())
    berries = []
    for i in range(n):
        a, b = map(int, input().split())
        berries.append((a, b))
    return n, berries


def max_height(n, berries: list):
    buf_h = 0
    for i in range(n):
        a, b = berries[i]
        delta = a - b
        if delta > 0:
            buf_h += a
            buf_h -= b
    last_day_i = 0
    max_h = buf_h
    for i in range(n):
        a, b = berries[i]
        delta = a - b
        if delta >= 0:
            if buf_h + b > max_h:
                max_h = buf_h + b
                last_day_i = i
        else:
            if buf_h + a > max_h:
                max_h = buf_h + a
                last_day_i = i
    ans = []
    for i in range(n):
        a, b = berries[i]
        delta = a - b
        if delta > 0 and i != last_day_i:
            ans.append(i + 1)
    ans.append(last_day_i + 1)
    for i in range(n):
        a, b = berries[i]
        delta = a - b
        if delta <= 0 and i != last_day_i:
            ans.append(i + 1)
    return max_h, ' '.join(map(str, ans))


def main():
    print(*max_height(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
