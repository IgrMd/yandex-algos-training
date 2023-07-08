from collections import defaultdict
import sys


def read_input():
    text = sys.stdin.readlines()
    return text


def most_used_word(text):
    counters = defaultdict(int)
    max_used_count = 0
    max_used_word = ''
    for line in text:
        for word in line.split():
            counters[word] += 1
            if max_used_count < counters[word]:
                max_used_count = counters[word]
                max_used_word = word
            elif max_used_count == counters[word]:
                max_used_word = min(max_used_word, word)
    return max_used_word


def main():
    print(most_used_word(read_input()))


if __name__ == '__main__':
    main()
