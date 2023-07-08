import sys
from collections import defaultdict


def read_input():
    n, case_sensitive, start_with_digit = input().split()
    n = int(n)
    case_sensitive = case_sensitive == 'yes'
    start_with_digit = start_with_digit == 'yes'
    keywords = set()
    for _ in range(n):
        word = input()
        if not case_sensitive:
            word = word.lower()
        keywords.add(word)
    raw_text = sys.stdin.readlines()
    text = []
    for line in raw_text:
        line = line.strip()
        if not case_sensitive:
            line = line.lower()
        text.append(line)
    return n, case_sensitive, start_with_digit, keywords, text


def get_alpha(case_sensitive):
    alphabet = {'_'}
    for c in range(ord('0'), ord('9') + 1):
        alphabet.add(chr(c))
    for c in range(ord('a'), ord('z') + 1):
        alphabet.add(chr(c))
    if case_sensitive:
        for c in range(ord('A'), ord('Z') + 1):
            alphabet.add(chr(c))
    return alphabet


def get_token_start(j: int, text: str, start_with_digit: bool, alphabet: set):
    i = j
    while i < len(text) and text[i] not in alphabet:
        i += 1
    if i < len(text) and not start_with_digit and text[i].isdigit():
        j = get_token_end(i, text, alphabet)
        return get_token_start(j, text, start_with_digit, alphabet)
    else:
        return i


def get_token_end(i: int, text: str, alphabet: set):
    j = i
    while j < len(text) and text[j] in alphabet:
        j += 1
    return j


def form_identificators(start_with_digit, text: str, alphabet, token_counter, keywords):
    i = get_token_start(0, text, start_with_digit, alphabet)
    j = get_token_end(i, text, alphabet)
    while i < len(text):
        token = text[i:j]
        if not token.isdigit() and token not in keywords:
            token_counter[token] += 1
        i = get_token_start(j, text, start_with_digit, alphabet)
        j = get_token_end(i, text, alphabet)


def identificators(n, case_sensitive, start_with_digit, keywords, text):
    alphabet = get_alpha(case_sensitive)
    token_counter = defaultdict(int)
    for line in text:
        form_identificators(start_with_digit, line, alphabet, token_counter, keywords)
    most_used = ''
    max_count = 0
    for token, count in token_counter.items():
        if max_count < count:
            max_count = count
            most_used = token
    return most_used


def main():
    print(identificators(*read_input()))


if __name__ == '__main__':
    main()
