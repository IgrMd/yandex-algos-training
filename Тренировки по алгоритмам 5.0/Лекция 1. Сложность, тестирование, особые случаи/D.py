FIGURES = 'RB'
FIELD_SIZE = 8


def read_input():
    field = [list(input().strip()) for _ in range(FIELD_SIZE)]
    return field


def unbeaten_cells(field):
    for row in range(FIELD_SIZE):
        for col in range(FIELD_SIZE):
            match field[row][col]:
                case 'B':  # bishop
                    row_l, col_t = row - 1, col - 1
                    while row_l >= 0 and col_t >= 0:
                        if field[row_l][col_t] in FIGURES:
                            break
                        if field[row_l][col_t] == '*':
                            field[row_l][col_t] = '_'
                        row_l -= 1
                        col_t -= 1
                    row_l, col_b = row - 1, col + 1
                    while row_l >= 0 and col_b < FIELD_SIZE:
                        if field[row_l][col_b] in FIGURES:
                            break
                        if field[row_l][col_b] == '*':
                            field[row_l][col_b] = '_'
                        row_l -= 1
                        col_b += 1

                    row_r, col_t = row + 1, col - 1
                    while row_r < FIELD_SIZE and col_t >= 0:
                        if field[row_r][col_t] in FIGURES:
                            break
                        if field[row_r][col_t] == '*':
                            field[row_r][col_t] = '_'
                        row_r += 1
                        col_t -= 1

                    row_r, col_b = row + 1, col + 1
                    while row_r < FIELD_SIZE and col_b < FIELD_SIZE:
                        if field[row_r][col_b] in FIGURES:
                            break
                        if field[row_r][col_b] == '*':
                            field[row_r][col_b] = '_'
                        row_r += 1
                        col_b += 1

                case 'R':  # rook
                    l = col - 1
                    while l >= 0:
                        if field[row][l] in FIGURES:
                            break
                        if field[row][l] == '*':
                            field[row][l] = '_'
                        l -= 1
                    r = col + 1
                    while r < FIELD_SIZE:
                        if field[row][r] in FIGURES:
                            break
                        if field[row][r] == '*':
                            field[row][r] = '_'
                        r += 1

                    t = row - 1
                    while t >= 0:
                        if field[t][col] in FIGURES:
                            break
                        if field[t][col] == '*':
                            field[t][col] = '_'
                        t -= 1
                    b = row + 1
                    while b < FIELD_SIZE:
                        if field[b][col] in FIGURES:
                            break
                        if field[b][col] == '*':
                            field[b][col] = '_'
                        b += 1
    answer = 0
    for row in field:
        for c in row:
            answer += c == '*'
    # for row in field:
    #     print(' '.join(row))
    return answer


def main():
    print(unbeaten_cells(read_input()))


if __name__ == '__main__':
    main()
