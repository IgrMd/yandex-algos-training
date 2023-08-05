def read_input():
    some_string = input()
    return some_string


def palindrome(some_string: str):
    if len(some_string) < 2:
        return 0
    mid = len(some_string) // 2
    l = 0
    r = len(some_string) - 1
    count = 0
    while l < r:
        if some_string[l] != some_string[r]:
            count += 1
        l += 1
        r -= 1
    return count


def main():
    print(palindrome(read_input()))


if __name__ == '__main__':
    main()
