def input_read():
    n, k = [int(x) for x in input().split()]
    return n, k


def grasshopper(n, k):
    answ = [0] * n
    answ[0] = 1
    for i in range(1, n):
        j = 1
        while j <= k and i - j >= 0:
            answ[i] += answ[i - j]
            j += 1
    return answ[-1]


def main():
    print(grasshopper(*input_read()))


if __name__ == '__main__':
    main()
