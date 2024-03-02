def read_input():
    l, x1, v1, x2, v2 = list(map(int, input().split()))
    return l, x1, v1, x2, v2


def equal_dist(l, x1, v1, x2, v2):
    if x1 == x2:
        return ['YES', 0]
    if v1 == v2 == 0:
        if x1 == x2:
            return ['YES', 0]
        else:
            return ['NO']
    if v1 < 0 and v2 < 0:
        v1, v2 = abs(v1), abs(v2)
        x1, x2 = l - x1, l - x2
    if x2 > x1:
        x1, x2 = x2, x1
        v1, v2 = v2, v1
    pos_t = []
    if v1 != -v2:
        t1 = (l - x1 - x2) / (v1 + v2)
        if t1 > 0:
            pos_t.append(t1)
        t3 = (2 * l - x1 - x2) / (v1 + v2)
        if t3 > 0:
            pos_t.append(t3)
    if v1 * v2 < 0:
        t2 = (l - x1 + x2) / (v1 - v2)
        if t2 > 0:
            pos_t.append(t2)
    if v2 > v1:
        t4 = (x1 - x2) / (v2 - v1)
        pos_t.append(t4)
    return ['YES', min(pos_t)] if len(pos_t) else ['NO']


def equal(ans1, ans2):
    if ans1[0] != ans2[0] or abs(ans1[1] - ans2[1]) > 1e-9:
        print(f'{ans1[0]} != {ans2[0]} or abs({ans1[1]} - {ans2[1]}) > 1e-6')
        return False
    return True


assert equal(equal_dist(72, 20, -38121735, 66, 288888467), ['YES', 0.0000000795])
assert equal(equal_dist(615143346, 79387687, -80123649, 306422480, -80123649), ['YES', 2.4075923389360363])
assert equal(equal_dist(6, 3, 1, 1, 1), ['YES', 1.0])
assert equal(equal_dist(12, 8, 10, 5, 20), ['YES', 0.3])
assert equal(equal_dist(5, 0, 0, 1, 2), ['YES', 2.0])
assert equal(equal_dist(10, 7, -3, 1, 4), ['YES', 0.8571428571])
print('tests passed')


def main():
    print(*equal_dist(*read_input()), sep='\n')


if __name__ == '__main__':
    main()
