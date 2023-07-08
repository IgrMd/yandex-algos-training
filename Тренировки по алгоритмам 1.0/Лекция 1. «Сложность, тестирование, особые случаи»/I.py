def prisoner(A, B, C, D, E):
    lst = [[A, B], [A, C], [B, C]]
    for a, b in lst:
        if (a <= D and b <= E) or (a <= E and b <= D):
            return 'YES'
    return 'NO'


assert prisoner(1, 1, 1, 1, 1) == 'YES'
assert prisoner(2, 2, 2, 1, 1) == 'NO'


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(prisoner(A, B, C, D, E))


if __name__ == '__main__':
    main()
