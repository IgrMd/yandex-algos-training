from dataclasses import dataclass


@dataclass
class Item:
    name: str
    m: int


def read_input():
    n, d = map(int, input().split())
    items = []
    for _ in range(n):
        name, m = input().split()
        items.append(Item(name, int(m)))
    return n, d, items


def asceticism(n: int, d: int, items: list[Item], ):
    items.sort(key=lambda x: x.m)
    max_mi = items[-1].m
    dp: list[list] = []
    dp.append([None] * (max_mi + 1))
    dp[0][0] = 0
    for i in range(n):
        if i > 0:
            dp.append(dp[-1].copy())
        item = items[i]
        row = dp[i]
        if item.m <= d:
            for mi in range(max_mi - item.m, -1, -1):
                if row[mi] is None:
                    continue
                if row[mi + item.m] is None:
                    row[mi + item.m] = row[mi] + 1
                else:
                    row[mi + item.m] = min(row[mi] + 1, row[mi + item.m])
            continue
        else:
            for mi in range(item.m - d, item.m):
                if row[mi] is None:
                    continue
                if row[item.m] is None:
                    row[item.m] = row[mi] + 1
                else:
                    row[item.m] = min(row[mi] + 1, row[item.m])
            buf = row[item.m]
            if buf is None:
                break
            for mi in range((max_mi - item.m), -1, -1):
                if mi == item.m:
                    continue
                if row[mi] is None:
                    continue
                if row[mi + item.m] is None:
                    row[mi + item.m] = row[mi] + buf
                else:
                    row[mi + item.m] = min(row[mi] + buf, row[mi + item.m])
    ans = []
    ans_count = 0
    for i in range(n):
        item = items[i]
        if dp[i][item.m] is None:
            break
        ans_count += dp[i][item.m]
        ans.append(item.name)
    ans.sort()
    print(len(ans), ans_count)
    print(*ans, sep='\n')


def main():
    asceticism(*read_input())


if __name__ == '__main__':
    main()
