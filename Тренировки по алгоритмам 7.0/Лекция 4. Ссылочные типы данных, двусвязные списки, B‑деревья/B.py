class Item:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, val):
        new_item = Item(val)
        if self.size == 0:
            self.head = self.tail = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        val = self.head.val
        if self.size == 1:
            self.clear()
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        return val

    def top(self):
        if self.size > 0:
            return self.head.val
        return None

    def back(self):
        if self.size > 0:
            return self.tail.val
        return None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


queue = Queue()


def push(n):
    queue.push(n)
    print('ok')


def pop():
    if len(queue):
        print(queue.pop())
    else:
        print('error')


def back():
    if len(queue):
        print(queue.back())
    else:
        print('error')


def front():
    if len(queue):
        print(queue.top())
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
    while True:
        cmd = input().split()
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
        elif cmd[0] == 'exit':
            break
    exit()


if __name__ == '__main__':
    main()
