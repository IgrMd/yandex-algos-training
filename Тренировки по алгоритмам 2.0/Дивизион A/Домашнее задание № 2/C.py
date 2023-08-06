def read_input():
    n = int(input())
    chess_board = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        chess_board[x][y] = 1
    return chess_board


def neighbours_cut(chess_board: list[list[int]], x: int, y: int):
    count = 0
    diff = ((-1, 0), (0, -1), (0, 1), (1, 0))
    for dx, dy in diff:
        count += not chess_board[x + dx][y + dy]
    return count


def perimeter_cut(chess_board: list[list[int]]):
    perimeter = 0
    for x in range(len(chess_board)):
        line = chess_board[x]
        for y in range(len(line)):
            if line[y] == 1:
                perimeter += neighbours_cut(chess_board, x, y)
    return perimeter


def main():
    print(perimeter_cut(read_input()))


if __name__ == '__main__':
    main()
