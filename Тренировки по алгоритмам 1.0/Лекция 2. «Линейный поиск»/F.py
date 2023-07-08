def read_input():
    n = int(input())
    inp_lst = [int(x) for x in input().split()]
    return inp_lst


def is_symmetric(begin, end, seq):
    if end - begin < 2:
        return True
    end -= 1
    while end - begin > 0:
        if seq[begin] != seq[end]:
            return False
        begin += 1
        end -= 1
    return True


def check_symmetry(sequence):
    n = len(sequence)
    if n < 2:
        return 0,
    if n == 2:
        return (0,) if sequence[0] == sequence[1] else (1, sequence[0])
    begin, end = 0, n
    while not is_symmetric(begin, end, sequence):
        begin += 1
    return begin, ' '.join(map(str, sequence[:begin][::-1]))


assert check_symmetry([1, 2, 3, 4, 5, 4, 3, 2, 1]) == (0, '')
assert check_symmetry([1, 2, 1, 2, 2]) == (3, '1 2 1')
assert check_symmetry([1, 2, 3, 4, 5]) == (4, '4 3 2 1')


def main():
    print(*check_symmetry(read_input()), sep='\n')


if __name__ == '__main__':
    main()
