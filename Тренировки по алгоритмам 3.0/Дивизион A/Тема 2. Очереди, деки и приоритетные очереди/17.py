from collections import deque

left, right = deque(), deque()


def normalize():
    while len(right) > len(left):
        left.append(right.popleft())


def come(priority, n):
    if priority == '+':
        right.append(n)
    else:
        right.appendleft(n)
    normalize()


def go():
    print(left.popleft())
    normalize()


def main():
    N = int(input())
    for i in range(N):
        cmd = input().split()
        if cmd[0] == '-':
            go()
        else:
            come(cmd[0], int(cmd[1]))


if __name__ == '__main__':
    main()
