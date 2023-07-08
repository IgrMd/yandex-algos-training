def read_input():
    n = int(input())
    dictionary = set()
    for _ in range(n):
        dictionary.add(input().strip())
    homework = input().split()
    return n, dictionary, homework


def wrong_stresses(n, dictionary, homework):
    dictionary_lower = {s.lower() for s in dictionary}
    capitals = {chr(x) for x in range(ord('A'), ord('Z') + 1)}

    errors = 0
    for word in homework:
        if word in dictionary:
            continue
        if word.lower() in dictionary_lower:
            errors += 1
            continue
        capitals_count = 0
        for c in word:
            if c in capitals:
                capitals_count += 1
            if capitals_count > 1:
                break
        if capitals_count != 1:
            errors += 1
    return errors


def main():
    print(wrong_stresses(*read_input()))


if __name__ == '__main__':
    main()
