def read_input():
    n = int(input())
    diplomas = [int(x) for x in input().split()]
    return n, diplomas


def time_to_find_diploma(d: int, diplomas: list[int]):
    return sum(diplomas) - max(diplomas)


def main():
    print(time_to_find_diploma(*read_input()))


if __name__ == '__main__':
    main()
