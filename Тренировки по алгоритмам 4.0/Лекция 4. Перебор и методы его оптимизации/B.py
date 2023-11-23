def read_input():
    n = int(input().strip())
    return n


def check_dinosaurs(dinosaurs: list):
    for i in range(len(dinosaurs) - 1):
        for j in range(i + 1, len(dinosaurs)):
            row1, col1 = dinosaurs[i]
            row2, col2 = dinosaurs[j]
            if row1 == row2 or col1 == col2 or row1 + col1 == row2 + col2 or row1 - col1 == row2 - col2:
                return False
    return True


def place_dinosaurs(col, n, dinosaurs: list, permutations: list, rows: list):
    if col == n:
        return check_dinosaurs(dinosaurs)
    count = 0
    for row in range(n):
        if rows[row]:
            continue
        dinosaurs.append((row, col))
        if not check_dinosaurs(dinosaurs):
            dinosaurs.pop()
            continue
        rows[row] = True
        count += place_dinosaurs(col + 1, n, dinosaurs, permutations, rows)
        dinosaurs.pop()
        rows[row] = False
    return count


def lost_world(n):
    dinosaurs = []
    permutations = []
    rows = [False for _ in range(n)]
    return place_dinosaurs(0, n, dinosaurs, permutations, rows)


def main():
    print(lost_world(read_input()))


if __name__ == '__main__':
    main()
