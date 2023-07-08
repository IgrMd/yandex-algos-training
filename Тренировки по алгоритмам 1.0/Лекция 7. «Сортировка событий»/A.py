def read_input():
    n, m = [int(x) for x in input().split()]
    teachers = [[int(x) for x in input().split()] for _ in range(m)]
    return n, m, teachers


def students_unattended(n: int, m: int, intervals: list):
    teachers = []
    for b, e in intervals:
        teachers.append((b, -1))
        teachers.append((e + 1, 1))
    teachers.sort()
    curr_students_attended = 0
    total_students_attended = 0
    for i in range(len(teachers)):
        if curr_students_attended > 0:
            total_students_attended += teachers[i][0] - teachers[i - 1][0]
        if teachers[i][1] == -1:
            curr_students_attended += 1
        if teachers[i][1] == 1:
            curr_students_attended -= 1
    return n - total_students_attended


def main():
    print(students_unattended(*read_input()))


if __name__ == '__main__':
    main()
