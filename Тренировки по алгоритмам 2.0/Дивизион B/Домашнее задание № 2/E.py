def read_input():
    n = int(input())
    diplomas = [int(x) for x in input().split()]
    return n, diplomas


def time_to_find_diploma(d: int, diplomas: list[int]):
    diplomas.sort()
    ans_t = 0
    for i in range(len(diplomas) - 1):
        ans_t += diplomas[i]
    return ans_t


def main():
    print(time_to_find_diploma(*read_input()))


if __name__ == '__main__':
    main()
