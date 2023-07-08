def read_input():
    n = int(input())
    words = {}
    for _ in range(n):
        word1, word2 = input().split()
        words[word1] = word2
        words[word2] = word1
    word = input()
    return words, word


def dictionary(words, word):
    return words[word]


def main():
    print(dictionary(*read_input()))


if __name__ == '__main__':
    main()
