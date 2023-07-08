def read_input():
    n = int(input())
    inp_lst = [int(x) for x in input().split()]
    target = int(input())
    return inp_lst, target


def closest(lst, target):
    if len(lst) == 0:
        return target
    if len(lst) == 1:
        return lst[0]
    nearest = lst[0]
    for x in lst:
        if abs(target - x) < abs(target - nearest):
            nearest = x
    return nearest


def main():
    print(closest(*read_input()))


if __name__ == '__main__':
    main()
