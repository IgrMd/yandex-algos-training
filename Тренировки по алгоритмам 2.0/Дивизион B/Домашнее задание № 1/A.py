def read_input():
    r = int(input())
    i = int(input())
    c = int(input())
    return r, i, c


def interactor(r, i, c):
    match i:
        case 0:
            if r != 0:
                return 3
            else:
                return c
        case 1:
            return c
        case 4:
            if r != 0:
                return 3
            else:
                return 4
        case 6:
            return 0
        case 7:
            return 1
    return i


def main():
    print(interactor(*read_input()))


if __name__ == '__main__':
    main()
