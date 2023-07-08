def read_input():
    n = int(input())
    inp_lst = [int(x) for x in input().split()]
    return inp_lst


def find_first_winner(throws):
    max_i = 0
    for i, x in enumerate(throws):
        if x > throws[max_i]:
            max_i = i
    return max_i


def place(throws):
    n = len(throws)
    if n < 3:
        return 0
    winner_i = find_first_winner(throws)
    vas_possible_trows = []
    for i in range(winner_i + 1, n - 1):
        if throws[i] % 10 == 5 and throws[i] > throws[i + 1]:
            vas_possible_trows.append(i)
    if len(vas_possible_trows) == 0:
        return 0
    vas_best_throw = max([throws[i] for i in vas_possible_trows])
    better_throws = 0
    for x in throws:
        if x > vas_best_throw:
            better_throws += 1
    return better_throws + 1


assert place([10, 20, 15, 10, 30, 5, 1]) == 6
assert place([15, 15, 10]) == 1
assert place([10, 15, 20]) == 0
assert place([10, 5, 1]) == 2
assert place([30, 5, 1, 30, 15, 2, 30, 25, 3]) == 4
assert place([555, 76, 661, 478, 889, 453, 555, 359, 601, 835]) == 5


def main():
    print(place(read_input()))


if __name__ == '__main__':
    main()
