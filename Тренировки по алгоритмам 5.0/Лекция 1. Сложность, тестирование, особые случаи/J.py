from collections import deque
from heapq import heappop, heappush


def read_input():
    data = []
    with open('input.txt', 'r') as fp:
        for n, line in enumerate(fp):
            if not n:
                w, h, c = list(map(int, line.split()))
                continue
            data.append(line.replace('\n', ''))
    return w, h, c, data


def parse_picture_token(picture_settings: dict, token: str):
    if token[0] == '(':
        token = token[1:]
    if token[-1] == ')':
        token = token[:-1]
    match token[0]:
        case 'l':
            picture_settings['layout'] = token[7]
        case 'w':
            picture_settings['width'] = int(token[7:-1]) if token[-1] == ')' else int(token[6:])
        case 'h':
            picture_settings['height'] = int(token[7:-1]) if token[-1] == ')' else int(token[7:])
        case 'd':
            picture_settings[token[0:2]] = int(token[3:-1]) if token[-1] == ')' else int(token[3:])


def parse_tokens(data: list[str]):
    tokens = deque()
    for line in data:
        if line == '':
            tokens.append(line)
            continue
        for token in line.split():
            tokens.append(token)
    return tokens


last_inserted_in_line = 0


def new_line(w: int, h: int, surrounded_pic_heap: list, lines: list):
    global last_inserted_in_line
    last_inserted_in_line = 0
    start_y = 0 if not len(lines) else lines[-1][0][0] + lines[-1][0][1]  # y coord + line height
    while len(surrounded_pic_heap) and surrounded_pic_heap[0][0] <= start_y:
        heappop(surrounded_pic_heap)
    lines.append(list())
    line = lines[-1]
    line.append(list((start_y, h)))
    line.append(list())
    fragments = line[1]
    fragments.append((0, 0, 1))
    fragments.append((w, w, 1))
    for y_max, x0, x1 in surrounded_pic_heap:
        fragments.append((x0, x1, 0))
    fragments.sort()
    return line


def try_insert_fragment(line: list, size: int, c: int):
    global last_inserted_in_line
    fragments = line[1]
    inserted = -1
    for i in range(len(fragments) - 1):
        if fragments[i][1] < last_inserted_in_line:
            continue
        space = (c if i > 0 else 0) * fragments[i][2]
        if fragments[i][1] + size + space <= fragments[i + 1][0]:
            if space:
                fragments.append((fragments[i][1], fragments[i][1] + space, 0))
            fragments.append((fragments[i][1] + space, fragments[i][1] + space + size, int(c > 0)))
            inserted = fragments[i][1] + space
            last_inserted_in_line = inserted
            fragments.sort()
            break
    return inserted


def insert_fragment(w: int, h: int, c: int, lines: list, line: list, surrounded_pic_heap: list, size: int):
    inserted = try_insert_fragment(line, size, c)
    while inserted == -1:
        line = new_line(w, h, surrounded_pic_heap, lines)
        inserted = try_insert_fragment(line, size, c)
    return inserted, line


def picture_coordinates(w: int, h: int, c: int, data: list[str]):
    tokens = parse_tokens(data)
    picture_settings = {
        'layout': '', 'dx': 0, 'dy': 0, 'width': 0, 'height': 0
    }
    surrounded_pic_heap = list()  # (y_max, x0, x1)
    lines = []
    line = new_line(w, h, surrounded_pic_heap, lines)
    last_x = 0
    last_y = 0
    while len(tokens):
        token = tokens.popleft()
        if token == '':  # new paragraph
            line = new_line(w, h, surrounded_pic_heap, lines)
            last_x = 0
            last_y = line[0][0]
            continue
        if token[0] == '(':  # picture start
            while token[-1] != ')':
                token = tokens.popleft()
                parse_picture_token(picture_settings, token)
            width = picture_settings['width']
            height = picture_settings['height']
            match picture_settings['layout']:
                case 'e':
                    inserted, line = insert_fragment(w, h, c, lines, line, surrounded_pic_heap, width)
                    line[0][1] = max(line[0][1], height)
                    last_x = inserted + width
                    last_y = line[0][0]
                    print(inserted, line[0][0])
                case 's':
                    inserted, line = insert_fragment(w, h, 0, lines, line, surrounded_pic_heap, width)
                    heappush(surrounded_pic_heap, (line[0][0] + height, inserted, inserted + width))
                    last_x = inserted + width
                    last_y = line[0][0]
                    print(inserted, line[0][0])
                case 'f':
                    x = min(max(0, last_x + picture_settings['dx']), w - width)
                    y = last_y + picture_settings['dy']
                    last_x = x + width
                    last_y = y
                    print(x, y)
            continue
        # simple word
        inserted, line = insert_fragment(w, h, c, lines, line, surrounded_pic_heap, len(token) * c)
        last_x = inserted + len(token) * c
        last_y = line[0][0]


def main():
    picture_coordinates(*read_input())


if __name__ == '__main__':
    main()
