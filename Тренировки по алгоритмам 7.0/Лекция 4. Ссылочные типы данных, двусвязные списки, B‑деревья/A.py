class Item:
    def __init__(self, val, next_item=None):
        self.val = val
        self.next = next_item


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, val):
        new_item = Item(val, self.head)
        self.head = new_item
        self.size += 1

    def pop(self):
        if self.head is not None:
            val = self.head.val
            self.head = self.head.next
            self.size -= 1
            return val
        return None

    def top(self):
        if self.head is not None:
            return self.head.val
        return None

    def clear(self):
        self.head = None
        self.size = 0


stack = Stack()


def push(n):
    stack.push(n)
    print('ok')


def pop():
    if len(stack):
        print(stack.pop())
    else:
        print('error')


def back():
    if len(stack):
        print(stack.top())
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
