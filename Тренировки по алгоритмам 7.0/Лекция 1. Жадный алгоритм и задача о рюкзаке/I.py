from dataclasses import dataclass


def read_input():
    n, s = map(int, input().split())
    items = [Item(0, 0, 0)]
    max_v = 0
    for _ in range(n):
        items.append(Item(*map(int, input().split())))
        max_v += items[-1].v
    return n, s, items, max_v


@dataclass
class Item:
    v: int
    c: int
    p: int


def elastic_rover(n: int, s: int, items: list[Item], max_v: int):
    dp: list[list] = [[None] * (max_v + 1)]
    dp[0][0] = (0, 10 ** 9, 0)
    for item_i in range(1, n + 1):
        dp.append(dp[-1].copy())
        row = dp[item_i]
        item = items[item_i]
        for v_i in range(max_v - item.v, -1, -1):
            if row[v_i] is None:
                continue
            if item.p < v_i + item.v - s:
                continue
            pos_cost = row[v_i][0] + item.c
            pos_p = min(row[v_i][1], item.p)
            if row[v_i + item.v] is None:
                row[v_i + item.v] = (pos_cost, pos_p, item_i)
            if row[v_i + item.v][0] < pos_cost:
                row[v_i + item.v] = (pos_cost, pos_p, item_i)
            elif row[v_i + item.v][0] == pos_cost:
                if row[v_i + item.v][0] < pos_p:
                    row[v_i + item.v] = (pos_cost, pos_p, item_i)
    mem_col = 0
    mem_row = 0
    max_cost = 0
    for row in range(n + 1):
        for col in range(1, max_v + 1):
            if dp[row][col] is None:
                continue
            cost, p, _ = dp[row][col]
            if p < col - s:
                continue
            if cost > max_cost:
                max_cost = cost
                mem_row = row
                mem_col = col
    ans = []
    _, _, item_i = dp[mem_row][mem_col]
    while item_i > 0:
        ans.append(item_i)
        mem_col -= items[item_i].v
        _, _, item_i = dp[item_i - 1][mem_col]

    print(len(ans), max_cost)
    print(*ans[::-1])


def main():
    elastic_rover(*read_input())


if __name__ == '__main__':
    main()
