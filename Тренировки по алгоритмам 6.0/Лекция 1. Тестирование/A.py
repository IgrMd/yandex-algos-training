def read_input():
    x1, y1, x2, y2, x, y = [int(input()) for _ in range(6)]
    return x1, y1, x2, y2, x, y


def raft(x1, y1, x2, y2, x, y):
    raft_vertexes = [
        ('SW', x1, y1),
        ('NW', x1, y2),
        ('NE', x2, y2),
        ('SE', x2, y1),
    ]
    raft_edges = [
        ('W', x1, y1, x1, y2),
        ('E', x2, y1, x2, y2),
        ('S', x1, y1, x2, y1),
        ('N', x1, y2, x2, y2),
    ]
    dist = 10 ** 6
    ans = ''
    for name, raft_x, raft_y in raft_vertexes:
        cur_dist = (x - raft_x) ** 2 + (y - raft_y) ** 2
        if cur_dist < dist:
            dist = cur_dist
            ans = name
    for name, rex1, rey1, rex2, rey2 in raft_edges:
        if rex1 == rex2:
            if y < rey1 or y > rey2:
                continue
            cur_dist = (x - rex1) ** 2
        elif rey1 == rey2:
            if x < rex1 or x > rex2:
                continue
            cur_dist = (y - rey1) ** 2
        else:
            continue
        if cur_dist < dist:
            dist = cur_dist
            ans = name
    return ans


def main():
    print(raft(*read_input()))


if __name__ == '__main__':
    main()
