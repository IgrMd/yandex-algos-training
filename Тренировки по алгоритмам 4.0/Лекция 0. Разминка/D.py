def read_input():
    s1 = input().strip()
    s2 = input().strip()
    return s1, s2


def is_anagram(s1, s2):
    letters1 = [0] * 26
    letters2 = [0] * 26
    displ = ord('a')
    for string, letters in [(s1, letters1), (s2, letters2)]:
        for c in string:
            letters[ord(c) - displ] += 1
    if letters1 == letters2:
        return 'YES'
    else:
        return 'NO'


def main():
    print(is_anagram(*read_input()))


if __name__ == '__main__':
    main()
