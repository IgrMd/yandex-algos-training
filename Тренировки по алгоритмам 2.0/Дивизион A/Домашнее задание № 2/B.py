def read_input():
    x = input()
    z = input()
    return x, z


def check(x, z, z_i):
    x_i = len(x) - 1
    while x_i >= 0 and z_i >= 0 and x[x_i] == z[z_i]:
        x_i -= 1
        z_i -= 1
    return z_i < 0


def min_manual_string(x: str, z: str):
    x = x * (len(z) // len(x) + 1)
    z_i = len(z) - 1
    while z_i >= 0:
        if z[z_i] != x[-1]:
            z_i -= 1
            continue
        if check(x, z, z_i):
            return z[z_i + 1:]
        else:
            z_i -= 1
    return z


def main():
    print(min_manual_string(*read_input()))


if __name__ == '__main__':
    main()
