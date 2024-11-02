def read_input():
    n, k = map(int, input().split())
    coordinates = list(map(int, input().split()))
    return n, k, coordinates


def monuments(n, k, coordinates):
    r = 0
    ans = 0
    for l in range(n):
        while r < n and coordinates[r] - coordinates[l] <= k:
            r += 1
        ans += n - r
    return ans


def main():
    print(monuments(*read_input()))


if __name__ == '__main__':
    main()
