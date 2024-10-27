import enum
from dataclasses import dataclass, field
from typing import Any


def read_input():
    n = int(input())
    tablo = []
    for _ in range(n):
        tablo.append(input().strip())
    return n, tablo


def normalize(n, tablo: list[str]):
    min_x, min_y, max_x, max_y = n, n, 0, 0
    for y in range(len(tablo)):
        for x in range((len(tablo[y]))):
            if tablo[y][x] == '#':
                min_x = min(x, min_x)
                min_y = min(y, min_y)
                max_x = max(x, max_x)
                max_y = max(y, max_y)
    normalized = list(tablo[min_y:max_y + 1])
    for i in range(len(normalized)):
        normalized[i] = normalized[i][min_x: max_x + 1]
    return normalized


class RowType(enum.Enum):
    Other = ''
    Empty = '.'
    Full = '#'
    LefSide = '#.'
    RightSide = '.#'
    Middle = '.#.'
    Sides = '#.#'

    @classmethod
    def _missing_(cls, value: object) -> Any:
        return RowType.Other


@dataclass
class Block:
    char: str = ''
    count: int = 0


@dataclass
class Row:
    type: RowType = RowType.Other
    blocks: list[Block] = field(default_factory=list)


def parse_line(line: str) -> Row:
    row = Row()
    prev_char = line[0]
    count = 0
    for c in line:
        if c == prev_char:
            count += 1
            continue
        row.blocks.append(Block(prev_char, count))
        prev_char = c
        count = 1
    row.blocks.append(Block(prev_char, count))
    str_pattern = ''.join(map(lambda x: x.char, row.blocks))
    row.type = RowType(str_pattern)
    return row


def parse_symbol_parts(tablo: list[str]) -> list[Row]:
    result = []
    for line in tablo:
        row = parse_line(line)
        if row.type == RowType.Other or row.type == RowType.Empty:
            return []
        if not len(result):
            result = [row]
            continue
        if row.type != result[-1].type:
            result.append(row)
            continue
        if row.blocks != result[-1].blocks:
            return []
    return result


def sign(n: int, tablo: list[str]) -> str:
    normalized = normalize(n, tablo)
    rows = parse_symbol_parts(normalized)
    if not len(rows):
        return 'X'
    if len(rows) == 1 and rows[0].type == RowType.Full:
        return 'I'
    if len(rows) == 2:
        row1, row2 = rows
        if row1.type == RowType.LefSide and row2.type == RowType.Full:
            return 'L'
    if len(rows) == 3:
        row1, row2, row3 = rows
        if (row1.type, row2.type, row3.type) == (RowType.Full, RowType.Sides, RowType.Full):
            return 'O'
        elif (row1.type, row2.type, row3.type) == (RowType.Full, RowType.LefSide, RowType.Full):
            return 'C'
        elif (row1.type, row2.type, row3.type) == (RowType.Sides, RowType.Full, RowType.Sides):
            if row1.blocks != row3.blocks:
                return 'X'
            return 'H'
    if len(rows) == 4:
        row1, row2, row3, row4 = rows
        if (row1.type, row2.type, row3.type, row4.type) == (RowType.Full, RowType.Sides, RowType.Full, RowType.LefSide):
            if row2.blocks[0].count != row4.blocks[0].count:
                return 'X'
            return 'P'
    return 'X'


def main():
    print(sign(*read_input()))


if __name__ == '__main__':
    main()
