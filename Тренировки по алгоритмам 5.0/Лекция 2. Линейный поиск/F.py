def read_input():
    n = int(input())
    sectors = list(map(int, input().split()))
    a, b, k = map(int, input().split())
    return n, sectors, a, b, k


def wheel_of_fortune_prize(n, sectors: list, a, b, k):
    max_prize = 0
    reversed_sectors = [sectors[0]]
    reversed_sectors.extend(reversed(sectors[1:]))
    for cur_speed in range(a, min(a + n * k, b) + 1, k):
        sector_i = ((cur_speed - 1) // k) % n
        max_prize = max(max_prize, sectors[sector_i], reversed_sectors[sector_i])
    return max_prize


def main():
    print(wheel_of_fortune_prize(*read_input()))


if __name__ == '__main__':
    main()
