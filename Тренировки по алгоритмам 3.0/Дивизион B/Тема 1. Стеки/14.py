def input_read():
    n = int(input())
    lst = [int(x) for x in input().split()]
    return lst


opers = {'+': lambda x1, x2: x2 + x1,
         '-': lambda x1, x2: x2 - x1,
         '*': lambda x1, x2: x2 * x1}


def solve(road1):
    if len(road1) == 1:
        return 'YES' if road1[0] == 1 else 'NO'
    road2 = []
    bottom = []
    bottom.append(road1[0])
    for i in range(1, len(road1)):
        while len(bottom) and bottom[-1] < road1[i]:
            road2.append(bottom.pop())
        bottom.append(road1[i])

    while len(bottom):
        road2.append(bottom.pop())
    for i, x in enumerate(road2, 1):
        if i != x:
            return 'NO'
    return 'YES'


def main():
    print(solve(input_read()))


if __name__ == '__main__':
    main()
