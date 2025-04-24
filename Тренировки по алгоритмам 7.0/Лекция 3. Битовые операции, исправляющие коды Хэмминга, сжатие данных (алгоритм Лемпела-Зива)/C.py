def read_input():
    n = int(input().strip())
    a = list(map(int, input().split()))
    return n, a


def xor_permutation2(n: int, a: list[int]):
    buf = []
    max_x = max(a)
    max_len = 0
    while max_x > 0:
        max_len += 1
        max_x = max_x >> 1
    for x in a:
        buf.append([])
        for j in range(max_len):
            buf[-1].append(x & 1)
            x = x >> 1
    check = 0
    for x in a:
        check ^= x
    if check == 0:
        print(*a)
        return

    ind = []
    i = 0
    while check:
        if check & 1:
            ind.append(i)
        check = check >> 1
        i += 1
    if len(ind) % 2:
        print('impossible')
        return
    for i in range(0, len(ind), 2):
        i1 = ind[i]
        i2 = ind[i + 1]
        flag = False
        for row in buf:
            if row[i1] ^ row[i2]:
                row[i1], row[i2] = row[i2], row[i1]
                flag = True
                break
        if flag:
            continue
        for ind in (i1, i2):
            for row in buf:
                if row[ind] == 1 and row[-1] == 0:
                    row[ind], row[-1] = row[-1], row[ind]

    for i in range(n):
        row = buf[i]
        x = 0
        for j in row[::-1]:
            x = x << 1
            x |= j
        a[i] = x
    check = 0
    for x in a:
        check ^= x
    if check != 0:
        print('impossible')
    else:
        print(*a)


def xor_permutation(n: int, a: list[int]):
    buf = []
    max_x = max(a)
    max_len = 0
    while max_x > 0:
        max_len += 1
        max_x = max_x >> 1
    for x in a:
        cnt = x.bit_count()
        buf.append([1] * cnt)
    for i in range(max_len):
        cur_count = 0
        for row in buf:
            if i >= len(row):
                continue
            cur_count += row[i]
        if cur_count % 2 == 0:
            continue
        row_i = -1
        min_len = max_len
        for j in range(n):
            row = buf[j]
            if len(row) == max_len:
                continue
            if i >= len(row):
                continue
            if row[i] == 1 and len(row) < min_len:
                row_i = j
                min_len = len(row)
        if row_i != -1:
            row = buf[row_i]
            row[i] = 0
            row.append(1)
    ans = []
    for row in buf:
        x = 0
        for i in range(max_len):
            x = x << 1
            if i < len(row):
                x |= row[i]
        ans.append(x)
    check = 0
    for x in ans:
        check ^= x
    if check != 0:
        xor_permutation2(n, a)
    else:
        print(*ans)


def main():
    xor_permutation(*read_input())


if __name__ == '__main__':
    main()
