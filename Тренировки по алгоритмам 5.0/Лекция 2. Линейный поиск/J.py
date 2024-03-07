def read_input():
    m, n = map(int, input().split())  # rows, cols
    art = [list(input().strip()) for _ in range(m)]
    return m, n, art


def find_first_point(m, n, art):
    for row in range(m):
        for col in range(n):
            if art[row][col] == '#':
                return row, col
    return None


def check_line(start, end, line: list):
    has_left = False
    for i in range(start):
        if line[i] == '#':
            has_left = True
    for i in range(start, end + 1):
        if line[i] != '#':
            return False
    has_right = False
    for i in range(end + 1, len(line)):
        if line[i] == '#':
            has_right = True
    if has_right:
        return not has_left
    if has_left:
        return not has_right
    return True


def find_second_point(m, n, art, start):
    row = start[0]
    col = start[1]
    while col < n and art[row][col] == '#':
        col += 1
    col -= 1
    row += 1
    while row < m and check_line(start[1], col, art[row]):
        row += 1
    row -= 1
    return row, col


def fill(art, p1, p2, mark):
    for row in range(p1[0], p2[0] + 1):
        for col in range(p1[1], p2[1] + 1):
            art[row][col] = mark


def check_art(m, n, art: list[list]):
    p1 = find_first_point(m, n, art)
    if not p1:
        return None
    p2 = find_second_point(m, n, art, p1)
    fill(art, p1, p2, 'a')
    p3 = find_first_point(m, n, art)
    if not p3:
        if p1 == p2:
            return None
        if p1[0] != p2[0]:
            fill(art, p1, (p1[0], p2[1]), 'b')
        else:
            fill(art, p1, (p2[0], p1[1]), 'b')
        return art
    p4 = find_second_point(m, n, art, p3)
    fill(art, p3, p4, 'b')
    return None if find_first_point(m, n, art) else art


def main():
    art = check_art(*read_input())
    if not art:
        print('NO')
    else:
        print('YES')
        for row in art:
            print(''.join(row))


if __name__ == '__main__':
    main()
