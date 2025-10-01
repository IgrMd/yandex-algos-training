def read_input():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input().strip())
    return n, m, matrix


def five_in_a_row(n, m, matrix):
    for row in range(n):
        o_cnt, x_cnt = 0, 0
        for col in range(m):
            if matrix[row][col] == 'X':
                x_cnt += 1
                o_cnt = 0
            elif matrix[row][col] == 'O':
                x_cnt = 0
                o_cnt += 1
            else:
                x_cnt = o_cnt = 0
            if x_cnt == 5 or o_cnt == 5:
                return 'Yes'
    for col in range(m):
        o_cnt, x_cnt = 0, 0
        for row in range(n):
            if matrix[row][col] == 'X':
                x_cnt += 1
                o_cnt = 0
            elif matrix[row][col] == 'O':
                x_cnt = 0
                o_cnt += 1
            else:
                x_cnt = o_cnt = 0
            if x_cnt == 5 or o_cnt == 5:
                return 'Yes'
    for diag in range(n + m - 1):
        row = min(diag, n - 1)
        col = diag - row
        o_cnt, x_cnt = 0, 0
        while row >= 0 and col < m:
            if matrix[row][col] == 'X':
                x_cnt += 1
                o_cnt = 0
            elif matrix[row][col] == 'O':
                x_cnt = 0
                o_cnt += 1
            else:
                x_cnt = o_cnt = 0
            if x_cnt == 5 or o_cnt == 5:
                return 'Yes'
            row -= 1
            col += 1
    for diag in range(n + m - 1):
        row = max(0, diag - n - 1)
        col = max(0, m - 1 - diag)
        o_cnt, x_cnt = 0, 0
        while row < n and col < m:
            if matrix[row][col] == 'X':
                x_cnt += 1
                o_cnt = 0
            elif matrix[row][col] == 'O':
                x_cnt = 0
                o_cnt += 1
            else:
                x_cnt = o_cnt = 0
            if x_cnt == 5 or o_cnt == 5:
                return 'Yes'
            row += 1
            col += 1
    return 'No'


def main():
    print(five_in_a_row(*read_input()))


if __name__ == '__main__':
    main()
