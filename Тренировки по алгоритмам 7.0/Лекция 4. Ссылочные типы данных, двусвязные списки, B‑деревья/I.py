from dataclasses import dataclass


@dataclass
class Item:
    prev: int
    val: int


def read_input():
    n = int(input().strip())
    requests = []
    for _ in range(n):
        a, b = input().split()
        requests.append((int(a), int(b)))
    return n, requests


def clone_snowmans(n: int, requests: list[tuple[int, int]]):
    snowmans: list[Item] = []
    snowmans.append(Item(0, 0))
    for t, m in requests:
        if m == 0:
            prev = snowmans[t]
            while prev.prev != 0 and prev.val == 0:
                prev = snowmans[prev.prev]
            snowmans.append(Item(prev.prev, 0))
        else:
            snowmans.append(Item(t, m))

    for i in range(1, len(snowmans)):
        snowman = snowmans[i]
        snowman.val += snowmans[snowman.prev].val
    ans = 0
    for s in snowmans:
        ans += s.val
    return ans


def main():
    print(clone_snowmans(*read_input()))


if __name__ == '__main__':
    main()
