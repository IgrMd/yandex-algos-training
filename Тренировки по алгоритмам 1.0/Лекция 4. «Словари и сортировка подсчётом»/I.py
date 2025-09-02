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
        capitals_met = False
        for c in word:
            if c in capitals:
                if capitals_met:
                    errors += 1
                    break
                else:
                    capitals_met = True
        if not capitals_met:
            errors += 1
    return errors


def main():
    print(wrong_stresses(*read_input()))


if __name__ == '__main__':
    main()
