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
    dp: list = [None] * (max_mi + 1)
    dp[0] = 0
    for i in range(n):
        item = items[i]
        if item.m <= d:
            for mi in range(max_mi - item.m, -1, -1):
                if dp[mi] is None:
                    continue
                if dp[mi + item.m] is None:
                    dp[mi + item.m] = dp[mi] + 1
                else:
                    dp[mi + item.m] = min(dp[mi] + 1, dp[mi + item.m])
            continue
        else:
            for mi in range(item.m - d, item.m):
                if dp[mi] is None:
                    continue
                if dp[item.m] is None:
                    dp[item.m] = dp[mi] + 1
                else:
                    dp[item.m] = min(dp[mi] + 1, dp[item.m])
            buf = dp[item.m]
            if buf is None:
                break
            for mi in range((max_mi - item.m), -1, -1):
                if mi == item.m:
                    continue
                if dp[mi] is None:
                    continue
                if dp[mi + item.m] is None:
                    dp[mi + item.m] = dp[mi] + buf
                else:
                    dp[mi + item.m] = min(dp[mi] + buf, dp[mi + item.m])
    ans = []
    ans_count = 0
    for i in range(n):
        item = items[i]
        if dp[item.m] is None:
            break
        ans_count += dp[item.m]
        ans.append(item.name)
    ans.sort()
    return f'{len(ans)} {ans_count}\n' + "\n".join(ans)


def main():
    print(asceticism(*read_input()))


if __name__ == '__main__':
    main()
