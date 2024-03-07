def read_input():
    n = int(input())
    ships = []
    for _ in range(n):
        i, j = list(map(int, input().split()))
        ships.append((i - 1, j - 1))
    return n, ships


def moves_to_column(n, ships: list[list], target):
    column = [0] * n
    for s in ships:
        if s[1] == target:
            column[s[0]] = 1
    moves = 0
    for i in range(n):
        ship = ships[i]
        if ship[1] == target:
            continue
        moves += abs(target - ship[1])
        k = 0
        while column[k]:
            k += 1
        moves += abs(k - ship[0])
        column[k] = 1
    return moves


def move_ships(n, ships: list[list]):
    if n < 1:
        return 0
    ships.sort()
    min_moves = moves_to_column(n, ships, 0)
    for target in range(1, n):
        min_moves = min(min_moves, moves_to_column(n, ships, target))
    return min_moves


def main():
    print(move_ships(*read_input()))


if __name__ == '__main__':
    main()
