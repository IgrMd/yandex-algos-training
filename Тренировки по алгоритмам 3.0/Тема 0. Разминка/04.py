def read_input():
    n = int(input())
    k = int(input())
    row_p = int(input())
    seat_p = int(input())
    return n, k, row_p, seat_p


def get_seat(n, k, row_p, seat_p):
    index_p = (row_p - 1) * 2 + seat_p
    index_vplus = index_p + k
    index_vminus = index_p - k
    if index_vplus > n and index_vminus < 1:
        return -1,
    row_vm = (index_vminus + 1) // 2
    seat_vm = index_vminus - ((row_vm - 1) * 2)
    row_vp = (index_vplus + 1) // 2
    seat_vp = index_vplus - ((row_vp - 1) * 2)
    if index_vplus > n:
        return row_vm, seat_vm
    elif index_vminus < 1:
        return row_vp, seat_vp
    if row_p - row_vm < row_vp - row_p:
        return row_vm, seat_vm
    else:
        return row_vp, seat_vp


def main():
    print(*get_seat(*read_input()))


if __name__ == '__main__':
    main()
