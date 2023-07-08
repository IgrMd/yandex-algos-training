deque = []


def push_front(n):
    deque.insert(0, n)
    print('ok')


def push_back(n):
    deque.append(n)
    print('ok')


def pop_front():
    if len(deque):
        print(deque.pop(0))
    else:
        print('error')


def pop_back():
    if len(deque):
        print(deque.pop())
    else:
        print('error')


def back():
    if len(deque):
        print(deque[-1])
    else:
        print('error')


def front():
    if len(deque):
        print(deque[0])
    else:
        print('error')


def size():
    print(len(deque))


def clear():
    deque.clear()
    print('ok')


def exit():
    print('bye')


def main():
    cmd = input().split()
    while cmd[0] != 'exit':
        if cmd[0] == 'push_front':
            push_front(int(cmd[1]))
        elif cmd[0] == 'push_back':
            push_back(int(cmd[1]))
        elif cmd[0] == 'pop_front':
            pop_front()
        elif cmd[0] == 'pop_back':
            pop_back()
        elif cmd[0] == 'front':
            front()
        elif cmd[0] == 'back':
            back()
        elif cmd[0] == 'size':
            size()
        elif cmd[0] == 'clear':
            clear()
        cmd = input().split()
    exit()


if __name__ == '__main__':
    main()
