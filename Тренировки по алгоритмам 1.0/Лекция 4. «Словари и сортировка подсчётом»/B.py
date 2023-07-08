from collections import defaultdict
import sys


def read_input():
    text = sys.stdin.readlines()
    return text


def words_count(text):
    counters = defaultdict(int)
    answer = []
    for line in text:
        for word in line.split():
            answer.append(counters[word])
            counters[word] += 1
    return answer


def main():
    print(*words_count(read_input()))


if __name__ == '__main__':
    main()
