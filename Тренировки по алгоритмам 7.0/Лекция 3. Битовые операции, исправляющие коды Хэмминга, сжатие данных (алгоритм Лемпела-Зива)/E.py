def main():
    x, y = map(int, input().split())
    c = x ^ y
    print(c)
    x, c = map(int, input().split())
    y = c ^ x
    print(y)


if __name__ == '__main__':
    main()
