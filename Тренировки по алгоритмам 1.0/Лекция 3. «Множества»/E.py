def read_input():
    source = {int(x) for x in input().split()}
    target = {int(x) for x in input()}
    return source, target


def nums_needed(source: set, target: set):
    return len(target.difference(source))


def main():
    print(nums_needed(*read_input()))


if __name__ == '__main__':
    main()
