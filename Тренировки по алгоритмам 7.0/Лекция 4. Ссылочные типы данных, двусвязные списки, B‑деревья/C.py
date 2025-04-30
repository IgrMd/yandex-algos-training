class Item:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def push_front(self, val):
        new_item = Item(val)
        if self.size == 0:
            self.head = self.tail = new_item
        else:
            new_item.next = self.head
            self.head.prev = new_item
            self.head = new_item
        self.size += 1

    def push_back(self, val):
        new_item = Item(val)
        if self.size == 0:
            self.head = self.tail = new_item
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.size += 1

    def pop_front(self):
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

    def pop_back(self):
        if self.size == 0:
            return None
        val = self.tail.val
        if self.size == 1:
            self.clear()
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        return val

    def front(self):
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


deque = Deque()


def push_front(n):
    deque.push_front(n)
    print('ok')


def push_back(n):
    deque.push_back(n)
    print('ok')


def pop_front():
    if len(deque):
        print(deque.pop_front())
    else:
        print('error')


def pop_back():
    if len(deque):
        print(deque.pop_back())
    else:
        print('error')


def back():
    if len(deque):
        print(deque.back())
    else:
        print('error')


def front():
    if len(deque):
        print(deque.front())
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
    while True:
        cmd = input().split()
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
        elif cmd[0] == 'exit':
            break
    exit()


if __name__ == '__main__':
    main()
