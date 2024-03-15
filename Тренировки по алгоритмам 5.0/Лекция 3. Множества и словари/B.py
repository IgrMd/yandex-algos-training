from collections import defaultdict


def read_input():
    s1 = input().strip()
    s2 = input().strip()
    return s1, s2


def is_anagram(s1, s2):
    letters = defaultdict(int)
    for c in s1:
        letters[c] += 1
    for c in s2:
        letters[c] -= 1
        if letters[c] < 0:
            return 'NO'
    return 'YES' if sum(letters.values()) == 0 else 'NO'


def main():
    print(is_anagram(*read_input()))


if __name__ == '__main__':
    main()
