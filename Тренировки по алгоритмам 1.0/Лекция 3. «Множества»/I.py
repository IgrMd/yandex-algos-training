def read_input():
    n = int(input())
    students = [None] * n
    for student in range(n):
        m = int(input())
        students[student] = {input() for _ in range(m)}
    return n, students


def languages(n, students):
    any_student = set()
    for student in students:
        any_student.update(student)
    every_student = any_student.copy()
    for student in students:
        every_student.intersection_update(student)
    return any_student, every_student


def main():
    any_student, every_student = languages(*read_input())
    print(len(every_student))
    print(*every_student, sep='\n')
    print(len(any_student))
    print(*any_student, sep='\n')


if __name__ == '__main__':
    main()
