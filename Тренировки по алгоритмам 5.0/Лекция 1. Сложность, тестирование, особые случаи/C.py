def read_input():
    n = int(input())
    spaces_to_add = [int(input()) for _ in range(n)]
    return n, spaces_to_add


def button_pressed(n, spaces_to_add):
    ans = 0
    for spaces in spaces_to_add:
        ans += spaces // 4
        spaces_left = spaces % 4
        if spaces_left > 1:
            ans += 2
        else:
            ans += spaces_left
    return ans


def main():
    print(button_pressed(*read_input()))


if __name__ == '__main__':
    main()
