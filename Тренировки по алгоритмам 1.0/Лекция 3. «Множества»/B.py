def read_input():
    set1 = {int(x) for x in input().split()}
    set2 = {int(x) for x in input().split()}
    return set1, set2


def unique_nums_count(set1, set2):
    return sorted(set1.intersection(set2))


def main():
    print(*unique_nums_count(*read_input()))


if __name__ == '__main__':
    main()
