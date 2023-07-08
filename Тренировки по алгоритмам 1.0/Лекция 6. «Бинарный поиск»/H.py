def read_input():
    n, k = [int(x) for x in input().split()]
    wires = [int(input()) for _ in range(n)]
    return n, k, wires


def upper_bound(left: int, right: int, check_func, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check_func(mid, params):
            left = mid
        else:
            right = mid - 1
    return left


def check_wire_len(length, params):
    n, k, wires = params
    if k == 0:
        return True
    wire_count = 0
    for wire in wires:
        wire_count += wire // length
    return wire_count >= k


def max_wires_len(n, k, wires):
    length = upper_bound(0, max(wires), check_wire_len, (n, k, wires))
    return length


def main():
    print(max_wires_len(*read_input()))


if __name__ == '__main__':
    main()
