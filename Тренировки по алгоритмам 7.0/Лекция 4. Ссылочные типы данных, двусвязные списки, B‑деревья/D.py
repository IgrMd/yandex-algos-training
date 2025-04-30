class Item:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.val}'


class Windows:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def run(self, val):
        new_item = Item(val)
        new_item.next = self.head
        if self.size > 0:
            self.head.prev = new_item
        self.head = new_item
        self.size += 1
        return self.head.val

    def alt_tab(self, k: int):
        n = k % self.size
        if n == 0:
            return self.head.val
        cur: Item = self.head
        while n:
            cur = cur.next
            n -= 1
        cur.prev.next = cur.next
        if cur.next is not None:
            cur.next.prev = cur.prev
        cur.prev = None
        cur.next = self.head
        self.head.prev = cur
        self.head = cur
        return self.head.val


def main():
    win = Windows()
    n = int(input().strip())
    for _ in range(n):
        cmd = input().strip()
        if cmd[0:3] == 'Run':
            print(win.run(cmd[4:]))
        else:
            k = cmd.count('+Tab')
            print(win.alt_tab(k))


if __name__ == '__main__':
    main()
