def read_input():
    n = int(input().strip())
    return n


def rotate(n: int):
    ans = n
    mask1 = 1
    mask2 = 0
    count = 0
    while mask1 <= n:
        mask1 = mask1 << 1
        mask2 = mask2 << 1
        mask2 |= 1
        count += 1
    for i in range(count):
        n = n << 1
        bit = bool(n & mask1)
        n &= mask2
        n |= bit
        ans = max(ans, n)
    return ans


def main():
    print(rotate(read_input()))


if __name__ == '__main__':
    main()
