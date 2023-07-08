def read_input():
    n, r, c = [int(x) for x in input().split()]
    students = [int(input()) for _ in range(n)]
    return n, r, c, students


def lower_bound(left: int, right: int, check_func, params):
    while left < right:
        mid = (left + right) // 2
        if check_func(mid, params):
            right = mid
        else:
            left = mid + 1
    return left


def check_difference(difference, params):
    n, r, c, students = params
    i = 0
    brigades_count = 0
    while i + c - 1 < n:
        if students[i + c - 1] - students[i] > difference:
            i += 1
        else:
            brigades_count += 1
            i += c
    return brigades_count >= r


def max_wires_len(n, r, c, students: list[int]):
    students.sort()
    answer = lower_bound(0, students[-1] - students[0], check_difference, (n, r, c, students))
    return answer


def main():
    print(max_wires_len(*read_input()))


if __name__ == '__main__':
    main()
