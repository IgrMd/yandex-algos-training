def read_input():
    n = int(input().strip())
    return n


def solve(n):
    answer = 0
    i, j = 1, 1
    for _ in range(n):
        I = i ** 2
        J = j ** 3
        if I == J:
            i += 1
            j += 1
            answer = I
            continue
        elif I < J:
            answer = I
            i += 1
        else:
            answer = J
            j += 1
    return answer


def main():
    print(solve(read_input()))


if __name__ == '__main__':
    main()
