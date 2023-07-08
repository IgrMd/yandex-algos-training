def read_input():
    n = int(input())
    return n


def sub_sequence(n):
    dp = [0] * (n + 1)
    cubes = []
    i = 1
    while i ** 3 <= n:
        cubes.append(i ** 3)
        i += 1
    dp[0] = 0
    dp[1] = 1
    for num in range(2, n + 1):
        min_cube_count = dp[num - 1] + 1
        for cube in cubes:
            if num - cube < 0:
                break
            if dp[num - cube] + 1 < min_cube_count:
                min_cube_count = dp[num - cube] + 1
        dp[num] = min_cube_count
    return dp[n]


def main():
    print(sub_sequence(read_input()))


if __name__ == '__main__':
    main()
