import sys


def main():
    a = int(input().strip())
    ans = 0
    while a > 0:
        ans += 1 & a
        a = a >> 1
    print(ans)


if __name__ == '__main__':
    main()
