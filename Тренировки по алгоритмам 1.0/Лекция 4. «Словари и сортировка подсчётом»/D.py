def read_input():
    n = int(input())
    max_clicks = [int(x) for x in input().split()]
    k = int(input())
    clicks = [int(x) for x in input().split()]
    return n, k, max_clicks, clicks


def keyboard(n, k, max_clicks, clicks):
    counts = [0] * n
    for key in clicks:
        counts[key - 1] += 1
    for i in range(n):
        if max_clicks[i] < counts[i]:
            print('YES')
        else:
            print('NO')


def main():
    keyboard(*read_input())


if __name__ == '__main__':
    main()
