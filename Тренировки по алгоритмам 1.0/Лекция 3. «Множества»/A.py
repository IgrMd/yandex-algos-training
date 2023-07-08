def read_input():
    return [int(x) for x in input().split()]


def unique_nums_count(lst):
    return len(set(lst))


def main():
    print(unique_nums_count(read_input()))


if __name__ == '__main__':
    main()
