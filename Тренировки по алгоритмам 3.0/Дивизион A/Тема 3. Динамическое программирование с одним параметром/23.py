def read_input():
    n = int(input())
    return n


def triangle(n):
    if n % 2:
        return (n * (n + 2) * (2 * n + 1) - 1) // 8
    else:
        return n * (n + 2) * (2 * n + 1) // 8


def main():
    print(triangle(read_input()))


if __name__ == '__main__':
    main()
