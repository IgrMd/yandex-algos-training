def read_input():
    s = input().strip()
    n = int(input().strip())
    words = set()
    for _ in range(n):
        words.add(input().strip())
    return n, s, words


def dictionary(n: int, s: str, words: set[str]):
    if not s:
        return ''
    dp = [list() for _ in range(len(s) + 1)]
    for l in range(len(s)):
        for r in range(l + 1, len(s) + 1):
            substr = s[l:r]
            if substr in words:
                dp[r].append(l)
    ans = []

    def helper(r):
        if r == 0:
            return True
        for l in dp[r]:
            if helper(l):
                ans.append(s[l:r])
                return True
        return False

    helper(len(s))
    return ' '.join(ans)


def main():
    print(dictionary(*read_input()))


if __name__ == '__main__':
    main()
