def read_input():
    n = int(input())
    return n


def guess_num(n):
    possible_nums = {x for x in range(1, n + 1)}
    while True:
        line = input().lower()
        if line == 'help':
            return sorted(possible_nums)
        asked_set = {int(x) for x in line.split()}
        answer = input().lower()
        if answer == 'no':
            possible_nums.difference_update(asked_set)
        elif answer == 'yes':
            possible_nums.intersection_update(asked_set)


def main():
    print(*guess_num(read_input()))


if __name__ == '__main__':
    main()
