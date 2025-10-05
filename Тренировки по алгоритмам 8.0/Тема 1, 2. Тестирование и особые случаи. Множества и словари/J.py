class List:
    def __init__(self):
        self.arr = []
        self.begin = 0


def lists():
    n = int(input().strip())
    list_dict = dict()
    for _ in range(n):
        row = input().split()
        if row[0] == 'List' and row[2] == '=':
            name = row[1]
            new_list = List()
            if row[3] == 'new':
                new_list.arr = row[4][5:-1].split(sep=',')
            else:
                point = row[3].find('.')
                src_name = row[3][0:point]
                l, r = map(int, row[3][point + 9:-1].split(sep=','))
                l -= 1
                src_list = list_dict[src_name]
                new_list.arr = src_list.arr
                new_list.begin = src_list.begin + l
            list_dict[name] = new_list
            continue
        row = row[0]
        point = row.find('.')
        src_list = list_dict[row[0:point]]
        cmd = row[point + 1:point + 4]
        if cmd == 'set':
            index, val = map(int, row[point + 5:-1].split(sep=','))
            index -= 1
            src_list.arr[src_list.begin + index] = val
            continue
        val = int(row[point + 5:-1])
        if cmd == 'get':
            val -= 1
            print(src_list.arr[src_list.begin + val])
        if cmd == 'add':
            if src_list.begin != 0:
                continue
            src_list.arr.append(val)


def main():
    lists()


if __name__ == '__main__':
    main()
