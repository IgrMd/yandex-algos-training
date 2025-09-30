def read_input():
    a, b, c, v0, v1, v2 = map(int, input().split())
    return a, b, c, v0, v1, v2


def quests(a, b, c, v0, v1, v2):
    ans = []
    ans.append(a / v0 + a / v1 + b / v0 + b / v1)

    ans.append(a / v0 + c / v1 + b / v2)
    ans.append(b / v0 + c / v1 + a / v2)

    ans.append(a / v0 + c / v0 + c / v1 + a / v2)
    ans.append(b / v0 + c / v0 + c / v1 + b / v2)

    ans.append(a / v0 + a / v1 + a / v0 + c / v0 + c / v1 + a / v1)
    ans.append(b / v0 + b / v1 + b / v0 + c / v0 + c / v1 + b / v1)

    return min(ans)


def main():
    print(quests(*read_input()))


if __name__ == '__main__':
    main()
