from dataclasses import dataclass


def read_input():
    n = int(input().strip())
    table = SparceTable(list(map(int, input().split())))
    return table


@dataclass
class Range:
    l: int
    r: int


@dataclass
class Item:
    max: int
    index: int


class SparceTable:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.dp: list[list[Item]] = [[]]
        for i in range(self.n):
            self.dp[0].append(Item(arr[i], i))
        self.pows2 = []
        self.k, cur_max = 0, 1
        for i in range(self.n + 1):
            if cur_max < i:
                self.k += 1
                cur_max *= 2
            self.pows2.append(self.k)
        cur_seg_len, prev_len = 2, 1
        for i in range(1, self.k):
            self.dp.append([])
            j = 0
            while j + cur_seg_len <= self.n:
                if self.dp[i - 1][j].max > self.dp[i - 1][j + prev_len].max:
                    self.dp[i].append(self.dp[i - 1][j])
                else:
                    self.dp[i].append(self.dp[i - 1][j + prev_len])
                j += 1
            prev_len = cur_seg_len
            cur_seg_len *= 2

    def handle_request(self, request: Range):
        req_len = request.r - request.l + 1
        pow_of_2 = self.pows2[req_len] - 1 if req_len > 1 else 0
        new_r = request.r - 2 ** pow_of_2 + 1
        row = self.dp[pow_of_2]
        return row[request.l] if row[request.l].max > row[new_r].max else row[new_r]


def main():
    table = read_input()
    for _ in range(int(input().strip())):
        request = Range(*map(int, input().split()))
        request.l -= 1
        request.r -= 1
        print(table.handle_request(request).index + 1)


if __name__ == '__main__':
    main()
