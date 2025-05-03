class Item:
    def __init__(self, x: int, nxt=None, prv=None):
        self.val = x
        self.next = nxt
        self.prev = prv

    def __repr__(self):
        return str(self.val)


def read_input():
    n = int(input().strip())
    parts = list(map(int, input().split()))
    requests = []
    k = int(input().strip())
    for _ in range(k):
        a, b = input().split()
        requests.append((int(a), int(b)))
    return n, parts, requests


def river(n: int, parts: list[int], requests: list[tuple[int, int]]):
    curr_ans = 0
    head = None
    for x in parts[::-1]:
        if not head:
            head = Item(x)
        else:
            new_item = Item(x, head)
            head.prev = new_item
            head = new_item
        curr_ans += x * x
    ans = [curr_ans]
    head_id = 1
    for e, v in requests:
        while head_id != v:
            if head_id < v:
                head = head.next
                head_id += 1
            else:
                head = head.prev
                head_id -= 1
        curr_ans -= head.val * head.val
        if e == 1:
            if not head.prev:
                curr_ans -= head.next.val * head.next.val
                head.next.val += head.val
                head.next.prev = None
                head = head.next
                curr_ans += head.val * head.val
            elif not head.next:
                curr_ans -= head.prev.val * head.prev.val
                head.prev.val += head.val
                head.prev.next = None
                head = head.prev
                curr_ans += head.val * head.val
                head_id -= 1
            else:
                curr_ans -= head.prev.val * head.prev.val
                curr_ans -= head.next.val * head.next.val
                x1 = head.val // 2
                x2 = x1 + head.val % 2
                head.prev.val += x1
                head.next.val += x2
                curr_ans += head.prev.val * head.prev.val
                curr_ans += head.next.val * head.next.val
                head.prev.next = head.next
                head.next.prev = head.prev
                head = head.next
        if e == 2:
            x1 = head.val // 2
            x2 = x1 + head.val % 2
            curr_ans += x1 * x1
            curr_ans += x2 * x2
            new_item1 = Item(x1, None, head.prev)
            new_item2 = Item(x2, head.next, new_item1)
            new_item1.next = new_item2
            if head.prev:
                head.prev.next = new_item1
            if head.next:
                head.next.prev = new_item2
            head = new_item1
        ans.append(curr_ans)
    return ans


def main():
    print(*river(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
