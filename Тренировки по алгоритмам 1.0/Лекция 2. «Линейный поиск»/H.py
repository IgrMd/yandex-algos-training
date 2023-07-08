def read_input():
    inp_lst = [int(x) for x in input().split()]
    return inp_lst


def max_factors3(sequence):
    if len(sequence) == 3:
        return sequence
    max1 = sequence[0]
    max2 = sequence[1]
    max3 = sequence[2]
    if max3 > max2:
        max3, max2 = max2, max3
    if max2 > max1:
        max2, max1 = max1, max2
    if max3 > max2:
        max3, max2 = max2, max3

    min1 = min(sequence[0], sequence[1])
    min2 = max(sequence[0], sequence[1])

    for i in range(2, len(sequence)):
        elem = sequence[i]
        if i > 2:
            if elem > max1:
                max3 = max2
                max2 = max1
                max1 = elem
            elif elem > max2:
                max3 = max2
                max2 = elem
            elif elem > max3:
                max3 = elem
        if elem < min1:
            min2 = min1
            min1 = elem
        elif elem < min2:
            min2 = elem
    if max1 * max2 * max3 >= min1 * min2 * max1:
        return max1, max2, max3
    else:
        return min1, min2, max1


def test():
    assert sorted(max_factors3([3, 5, 1, 7, 9, 0, 9, -3, 10])) == sorted([10, 9, 9])
    assert sorted(max_factors3([-5, -30000, -12])) == sorted([-5, -12, -30000])
    assert sorted(max_factors3([1, 2, 3])) == sorted([3, 2, 1])
    assert sorted(max_factors3([-2, 7, 10, 12])) == sorted([7, 10, 12])


def main():
    test()
    print(*max_factors3(read_input()))


if __name__ == '__main__':
    main()
