def read_input():
    inp_lst = [int(x) for x in input().split()]
    return inp_lst


def neighbours(lst):
    if len(lst) < 3:
        return 0
    count = 0
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] > lst[i + 1]:
            count += 1
    return count


def main():
    print(neighbours(read_input()))


if __name__ == '__main__':
    main()
