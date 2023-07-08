def read_input():
    k = int(input())
    s = input().strip()
    return k, s


def robot_used_count(k, s):
    count = 0
    prevlen = 0
    for i in range(k, len(s)):
        if s[i] == s[i - k]:
            prevlen += 1
        else:
            prevlen = 0
        count += prevlen
    return count


def main():
    print(robot_used_count(*read_input()))


if __name__ == '__main__':
    main()
