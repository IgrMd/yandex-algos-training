def read_input():
    n, w, l = [int(x) for x in input().split()]
    blocks = []
    for _ in range(n):
        x1, y1, z1, x2, y2, z2 = [int(x) for x in input().split()]
        blocks.append((x1, y1, z1, x2, y2, z2))
    return n, w, l, blocks


def construction(n, w, l, blocks):
    events = []
    for i in range(n):
        x1, y1, z1, x2, y2, z2 = blocks[i]
        square = (x2 - x1) * (y2 - y1)
        block_id = i + 1
        events.append((z2, -1, square, block_id))
        events.append((z1, 1, square, block_id))
    events.sort()
    min_block_count = n + 1
    curr_block_count = 0
    construction_square = w * l
    curr_blocks_square = 0
    for event in events:
        coord, action, square, block_id = event
        if action == -1:
            curr_blocks_square -= square
            curr_block_count -= 1
        if action == 1:
            curr_blocks_square += square
            curr_block_count += 1
        if curr_blocks_square == construction_square:
            if curr_block_count < min_block_count:
                min_block_count = curr_block_count
    if min_block_count == n + 1:
        print('NO')
        return
    curr_blocks = set()
    for event in events:
        coord, action, square, block_id = event
        if action == -1:
            curr_blocks_square -= square
            curr_blocks.remove(block_id)
        if action == 1:
            curr_blocks_square += square
            curr_blocks.add(block_id)
        if curr_blocks_square == construction_square and min_block_count == len(curr_blocks):
            print('YES')
            print(min_block_count)
            print(*sorted(curr_blocks))
            return


def main():
    construction(*read_input())


if __name__ == '__main__':
    main()
