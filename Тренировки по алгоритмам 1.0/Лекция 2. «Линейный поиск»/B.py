def read_input():
    inp = []
    a = int(input())
    while a != -2e9:
        inp.append(a)
        a = int(input())
    return inp


def sequence(lst):
    const, asc, wasc, desc, wdesc = True, True, True, True, True
    if len(lst) == 0:
        return 'RANDOM'
    if len(lst) == 1:
        return 'CONSTANT'
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            const = False
        if lst[i] >= lst[i + 1]:
            asc = False
        if lst[i] > lst[i + 1]:
            wasc = False
        if lst[i] <= lst[i + 1]:
            desc = False
        if lst[i] < lst[i + 1]:
            wdesc = False
    if any([const, asc, wasc, desc, wdesc]):
        if const:
            return 'CONSTANT'
        if asc:
            return 'ASCENDING'
        if wasc:
            return 'WEAKLY ASCENDING'
        if desc:
            return 'DESCENDING'
        if wdesc:
            return 'WEAKLY DESCENDING'
    return 'RANDOM'


def main():
    print(sequence(read_input()))


if __name__ == '__main__':
    main()
