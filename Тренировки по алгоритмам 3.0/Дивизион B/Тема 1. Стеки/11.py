stack = []


def push(n):
    stack.append(n)
    print('ok')


def pop():
    if len(stack):
        print(stack.pop())
    else:
        print('error')


def back():
    if len(stack):
        print(stack[-1])
    else:
        print('error')


def size():
    print(len(stack))


def clear():
    stack.clear()
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
        elif cmd[0] == 'size':
            size()
        elif cmd[0] == 'clear':
            clear()
        cmd = input().split()
    exit()


if __name__ == '__main__':
    main()
