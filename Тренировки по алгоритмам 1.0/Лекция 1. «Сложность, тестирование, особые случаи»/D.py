def solve(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0:
        if c ** 2 == b:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    if (c ** 2 - b) % a == 0:
        return (c ** 2 - b) // a
    else:
        return 'NO SOLUTION'


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve(a, b, c))


if __name__ == '__main__':
    main()
