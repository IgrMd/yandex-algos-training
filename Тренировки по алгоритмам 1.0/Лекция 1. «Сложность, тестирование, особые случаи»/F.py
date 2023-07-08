def table(a1, b1, a2, b2):
    combinations = [[a1 + a2, max(b1, b2)],
                    [a1 + b2, max(b1, a2)],
                    [b1 + b2, max(a1, a2)],
                    [b1 + a2, max(a1, b2)]]
    return min(combinations, key=lambda x: x[0] * x[1])


def main():
    a1, b1, a2, b2 = list(map(int, input().split()))
    print(*table(a1, b1, a2, b2))


if __name__ == '__main__':
    main()
