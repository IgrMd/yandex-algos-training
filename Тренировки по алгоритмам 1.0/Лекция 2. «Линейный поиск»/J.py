def triangle():
    L = 30.0
    R = 4000.0
    n = int(input())
    f_prev = float(input())
    for _ in range(n - 1):
        f, res = input().split()
        f = float(f)
        if f < f_prev:
            if res == 'closer':
                R = min(R, f + abs(f - f_prev) / 2)
            if res == 'further':
                L = max(L, f_prev - abs(f - f_prev) / 2)
        if f_prev < f:
            if res == 'closer':
                L = max(L, f - abs(f - f_prev) / 2)
            if res == 'further':
                R = min(R, f_prev + abs(f - f_prev) / 2)
        f_prev = f
    print(L, R)


def main():
    triangle()


if __name__ == '__main__':
    main()
