def read_input():
    field = [[int(x) for x in input().split()] for _ in range(3)]
    return field


def is_all_eq(arr: list[int], target):
    for x in arr:
        if x != target:
            return False
    return True


def is_win(field: list[list], mark: int):
    for line in field:
        if is_all_eq(line, mark):
            return True
    if is_all_eq([field[i][i] for i in range(3)], mark):
        return True
    if is_all_eq([field[2 - i][i] for i in range(3)], mark):
        return True
    for i in range(3):
        if is_all_eq([field[j][i] for j in range(3)], mark):
            return True
    return False


def is_correct(field: list[list]):
    x_count = 0
    o_count = 0
    for line in field:
        for mark in line:
            match mark:
                case 1:
                    x_count += 1
                case 2:
                    o_count += 1
    if is_win(field, 1):
        return (x_count - o_count == 1) and not is_win(field, 2)
    if is_win(field, 2):
        return x_count == o_count
    return 0 <= (x_count - o_count) <= 1


def main():
    if is_correct(read_input()):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
