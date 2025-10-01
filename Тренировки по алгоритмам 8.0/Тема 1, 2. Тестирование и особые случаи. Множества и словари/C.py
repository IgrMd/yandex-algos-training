from collections import defaultdict


def read_input():
    return input().strip()


def cybersecurity(s: str):
    chars = defaultdict(int)
    for c in s:
        chars[c] += 1
    alphabet = ''
    for i in range(ord('a'), ord('z') + 1):
        alphabet += chr(i)
    ans = 1
    for c1 in range(len(alphabet) - 1):
        for c2 in range(c1 + 1, len(alphabet)):
            ans += chars[alphabet[c1]] * chars[alphabet[c2]]
    return ans


def main():
    print(cybersecurity(read_input()))


if __name__ == '__main__':
    main()
