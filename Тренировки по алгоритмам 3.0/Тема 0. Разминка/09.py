def read_input():
    pass


def get_elems_sum(matrix, x1, y1, x2, y2):
    summ = 0
    if x1 == y1 == 0:
        return matrix[x2][y2]
    if x1 == 0:
        return matrix[x2][y2] - matrix[x2][y1 - 1]
    if y1 == 0:
        return matrix[x2][y2] - matrix[x1 - 1][y2]
    return matrix[x2][y2] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2] + matrix[x1 - 1][y1 - 1]


def prepair(matrix, n, m):
    for j in range(1, m):
        matrix[0][j] += matrix[0][j - 1]
    for i in range(1, n):
        matrix[i][0] += matrix[i - 1][0]
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
prepair(matrix, 3, 3)
assert get_elems_sum(matrix, 2 - 1, 2 - 1, 3 - 1, 3 - 1) == 28
assert get_elems_sum(matrix, 1 - 1, 1 - 1, 2 - 1, 3 - 1) == 21


def main():
    n, m, k = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for j in range(n)]
    requests = [[(int(x) - 1) for x in input().split()] for j in range(k)]
    prepair(matrix, n, m)
    for request in requests:
        print(get_elems_sum(matrix, *request))
    # print(solve(*read_input()))


if __name__ == '__main__':
    main()
