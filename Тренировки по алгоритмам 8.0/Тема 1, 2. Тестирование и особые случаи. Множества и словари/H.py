from collections import defaultdict


def read_input():
    n, m = map(int, input().split())
    s = input().strip()
    pieces = []
    for i in range(m):
        pieces.append(input().strip())
    return n, m, s, pieces


def splitted_string(n, m, s, pieces):
    pieces_map = defaultdict(lambda: list())
    for num, piece in enumerate(pieces):
        pieces_map[piece].append(num + 1)
    i = 0
    ans = []
    piece_len = n // m
    for i in range(0, n, piece_len):
        ans.append(pieces_map[s[i:i + piece_len]].pop())
    return ans


def main():
    print(*splitted_string(*read_input()))


if __name__ == '__main__':
    main()
