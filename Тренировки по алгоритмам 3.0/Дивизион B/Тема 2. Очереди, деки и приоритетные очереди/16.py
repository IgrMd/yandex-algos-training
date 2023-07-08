queue = []


def push(n):
    queue.append(n)
    print('ok')


def pop():
    if len(queue):
        print(queue.pop(0))
    else:
        print('error')


def back():
    if len(queue):
        print(queue[-1])
    else:
        print('error')


def front():
    if len(queue):
        print(queue[0])
    else:
        print('error')


def size():
    print(len(queue))


def clear():
    queue.clear()
    print('ok')


def exit():
    print('bye')


def main():
    cmd = input().split()
    while cmd[0] != 'exit':
        if cmd[0] == 'push':
            push(int(cmd[1]))
        elif cmd[0] == 'pop':
            pop()
        elif cmd[0] == 'back':
            back()
        elif cmd[0] == 'front':
            front()
        elif cmd[0] == 'size':
            size()
        elif cmd[0] == 'clear':
            clear()
        cmd = input().split()
    exit()


if __name__ == '__main__':
    main()
