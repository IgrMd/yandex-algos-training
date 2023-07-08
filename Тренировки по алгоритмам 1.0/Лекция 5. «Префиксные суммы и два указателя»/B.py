def read_input():
    n, k = [int(x) for x in input().split()]
    cars = [int(x) for x in input().split()]
    return n, k, cars


def car_sets(n, k, cars):
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = cars[i - 1] + prefix_sums[i - 1]
    l, r = 0, 1
    sets_found = 0
    while l < r < len(prefix_sums):
        if prefix_sums[r] - prefix_sums[l] == k:
            sets_found += 1
            r += 1
        elif prefix_sums[r] - prefix_sums[l] > k:
            l += 1
            if r == l:
                r += 1
        elif prefix_sums[r] - prefix_sums[l] < k:
            r += 1

    return sets_found


def main():
    print(car_sets(*read_input()))


if __name__ == '__main__':
    main()
