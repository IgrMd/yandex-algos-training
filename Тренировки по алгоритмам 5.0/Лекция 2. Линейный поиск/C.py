def read_input():
    n = int(input())
    ropes = list(map(int, input().split()))
    return n, ropes


def min_rope_len(n, ropes):
    max_rope = max(ropes)
    sum_of_rest = sum(ropes) - max_rope
    return max_rope - sum_of_rest if max_rope > sum_of_rest else sum_of_rest + max_rope


def main():
    print(min_rope_len(*read_input()))


if __name__ == '__main__':
    main()
