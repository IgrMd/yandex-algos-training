from collections import defaultdict


def read_input():
    n = int(input())
    blocks = defaultdict(int)
    for _ in range(n):
        width, height = [int(x) for x in input().split()]
        blocks[width] = max(blocks[width], height)
    return blocks


def pyramid(blocks: dict):
    return sum(blocks.values())


def main():
    print(pyramid(read_input()))


if __name__ == '__main__':
    main()
