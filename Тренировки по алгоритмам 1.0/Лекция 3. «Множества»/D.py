from sys import stdin


def read_input():
    words = set()
    for line in stdin.readlines():
        words.update(line.split())
    return words


def words_count(words):

    return len(words)


def main():
    print(words_count(read_input()))


if __name__ == '__main__':
    main()
