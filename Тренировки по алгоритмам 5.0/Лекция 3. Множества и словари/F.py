def read_input():
    dictionary = set(input().split())
    text = input().split()
    return dictionary, text


def change_words(dictionary: set, text: list):
    for i in range(len(text)):
        word = text[i]
        for j in range(1, len(word)):
            found = False
            if word[0:j] in dictionary:
                text[i] = word[0:j]
                found = True
                break
            if found:
                break
    return text


def main():
    print(*change_words(*read_input()), sep=' ')


if __name__ == '__main__':
    main()
