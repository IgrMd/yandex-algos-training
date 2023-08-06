def read_input():
    n = int(input())
    ropes = [int(x) for x in input().split()]
    return n, ropes


def rope_len(n, ropes: list[int]):
    ropes.sort()
    max_rope = ropes[-1]
    min_sum = sum(ropes[0:-1])
    if max_rope > min_sum:
        return max_rope - min_sum
    else:
        return max_rope + min_sum


def main():
    print(rope_len(*read_input()))


if __name__ == '__main__':
    main()
