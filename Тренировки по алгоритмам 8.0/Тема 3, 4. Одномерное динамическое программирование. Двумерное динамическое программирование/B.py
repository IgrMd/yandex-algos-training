def read_input():
    return input().strip()


def camping(s: str):
    s = ' ' + s
    dpl = [float('inf')] * len(s)
    dpr = [float('inf')] * len(s)
    dpl[0] = 0
    dpr[0] = 1
    for i in range(1, len(s)):
        dpl[i] = dpl[i - 1] + 1 if s[i] in 'BL' else dpl[i - 1]
        dpr[i] = dpr[i - 1] + 1 if s[i] in 'BR' else dpr[i - 1]
        dpl[i] = min(dpl[i], dpr[i] + 1)
        dpr[i] = min(dpr[i], dpl[i] + 1)
    return dpr[-1]


def main():
    print(camping(read_input()))


if __name__ == '__main__':
    main()
