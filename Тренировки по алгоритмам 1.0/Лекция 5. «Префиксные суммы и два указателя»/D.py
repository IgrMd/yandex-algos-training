def read_input():
    n, r = [int(x.strip()) for x in input().strip().split()]
    monuments = [int(x.strip()) for x in input().strip().split()]
    return n, r, monuments


def monuments_count(n, r, monuments):
    count = 0
    right = 0
    for left in range(n):
        while right < n and monuments[right] - monuments[left] <= r:
            right += 1
        if right < n:
            count += n - right
    return count


assert monuments_count(4, 4, [1, 3, 5, 8]) == 2
assert monuments_count(5, 4, [1, 3, 5, 8, 9]) == 4
assert monuments_count(5, 4, [1, 3, 5, 8, 10]) == 5
assert monuments_count(10, 4, [1, 1, 1, 1, 2, 3, 4, 4, 4, 4]) == 0
assert monuments_count(3, 4, [1, 100, 200]) == 3
assert monuments_count(10, 54, [11, 38, 46, 49, 57, 59, 62, 65, 67, 72]) == 2


def main():
    print(monuments_count(*read_input()))


if __name__ == '__main__':
    main()
