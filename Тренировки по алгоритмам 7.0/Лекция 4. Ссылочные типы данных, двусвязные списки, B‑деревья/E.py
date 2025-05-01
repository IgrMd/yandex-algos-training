class Item:
    def __init__(self, i, val):
        self.i = i
        self.rating = val
        self.next = None
        self.prev = None
        self.kicked = 0

    def __repr__(self):
        return f'{self.i}: {self.rating}'


def read_input():
    n = int(input().strip())
    ratings = list(map(int, input().split()))
    return n, ratings


def weak_chain(n: int, rates: list[int]):
    players = [Item(i, x) for i, x in enumerate(rates)]
    for i in range(n):
        players[i].prev = players[i - 1]
        players[i].next = players[(i + 1) % n]
    left = n
    rnd = 1
    out = []
    to_check = set([i for i in range(n)])
    while True:
        if left < 3:
            break
        for i in to_check:
            cur = players[i]
            if cur.rating < cur.next.rating and cur.rating < cur.prev.rating:
                out.append(cur.i)
        if not out:
            break
        to_check.clear()
        for i in out:
            player = players[i]
            player.prev.next = player.next
            player.next.prev = player.prev
            player.kicked = rnd
            to_check.add(player.prev.i)
            to_check.add(player.next.i)
        left -= len(out)
        out.clear()
        rnd += 1
    ans = [x.kicked for x in players]
    return ans


def main():
    print(*weak_chain(*read_input()))


if __name__ == '__main__':
    main()
