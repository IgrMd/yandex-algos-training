def read_input():
    a = int(input().strip())
    b = int(input().strip())
    n = int(input().strip())
    return a, b, n


def students(a, b, n):
    min_b_students = b // n + (b % n > 0)
    if a > min_b_students:
        return 'Yes'
    return 'No'


def main():
    print(students(*read_input()))


if __name__ == '__main__':
    main()
