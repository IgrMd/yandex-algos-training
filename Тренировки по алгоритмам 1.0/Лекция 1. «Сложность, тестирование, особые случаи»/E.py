def entrance_and_floor(flat, flats_on_fl, m):
    floor_in_tower = (flat - 1) // flats_on_fl + 1
    entrance = (floor_in_tower - 1) // m + 1
    floor = (floor_in_tower - 1) % m + 1
    return entrance, floor


def check(k1, m, k2, p2, n2, flats_on_fl):
    entrance, floor = entrance_and_floor(k2, flats_on_fl, m)
    if entrance == p2 and floor == n2:
        return entrance_and_floor(k1, flats_on_fl, m)
    return -1, -1


def ambulance(k1, m, k2, p2, n2):
    p1 = -1
    n1 = -1
    found = False
    for flats_on_fl in range(1, max(k1, k2) + 1):
        p, n = check(k1, m, k2, p2, n2, flats_on_fl)
        if p != -1:
            found = True
            if p1 == -1:
                p1, n1 = p, n
            elif p1 != p and p1 != 0:
                p1 = 0
            elif n1 != n and n1 != 0:
                n1 = 0
    if found:
        return p1, n1
    else:
        return -1, -1


def main():
    k1, m, k2, p2, n2 = list(map(int, input().split()))
    print(*ambulance(k1, m, k2, p2, n2))


def test():
    assert ambulance(89, 20, 41, 1, 11) == (2, 3)
    assert ambulance(11, 1, 1, 1, 1) == (0, 1)
    assert ambulance(3, 2, 2, 2, 1) == (-1, -1)


if __name__ == '__main__':
    test()
    main()
