def friendship_won(n, table):
    l, r = 0, n - 1
    sdv, sdm = table[0], table[-1]
    ans = (abs(sdv - sdm), 1, n)

    def ans_update():
        nonlocal ans
        if abs(sdv - sdm) < ans[0]:
            ans = (abs(sdv - sdm), l + 1, r + 1)

    while r - l > 1:
        if sdv < sdm:
            l += 1
            sdv += table[l]
        elif sdm < sdv:
            r -= 1
            sdm += table[r]
        else:
            if table[l] < table[r]:
                l += 1
                sdv += table[l]
            else:
                r -= 1
                sdm += table[r]
        ans_update()
    return ans


def main():
    n = int(input().strip())
    table = list(map(int, input().split()))
    print(*friendship_won(n, table))


if __name__ == '__main__':
    main()
