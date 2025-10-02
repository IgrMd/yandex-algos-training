from collections import defaultdict


def read_input():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input().strip())
    return n, m, matrix


def plus_minus_question(n: int, m: int, matrix: list[list[str]]):
    rows = [0] * n
    cols = [0] * m
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == '-':
                rows[row] -= 1
                cols[col] -= 1
            elif matrix[row][col] == '+':
                rows[row] += 1
                cols[col] += 1
            elif matrix[row][col] == '?':
                rows[row] += 1
                cols[col] -= 1
    rows_cnt = defaultdict(lambda: list())
    cols_cnt = defaultdict(lambda: list())
    for row, row_sum in enumerate(rows):
        rows_cnt[row_sum].append(row)
    for col, col_sum in enumerate(cols):
        cols_cnt[col_sum].append(col)
    ans = float('-inf')
    max_row_sum = max(rows)
    min_col_sum = min(cols)
    for row in rows_cnt[max_row_sum]:
        for col in cols_cnt[min_col_sum]:
            if matrix[row][col] != '?':
                ans = max(ans, max_row_sum - min_col_sum)
            else:
                ans = max(ans, max_row_sum - min_col_sum - 2)
    return ans


def main():
    print(plus_minus_question(*read_input()))


if __name__ == '__main__':
    main()
