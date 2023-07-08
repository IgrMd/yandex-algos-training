from collections import defaultdict


def read_input():
    n, k = [int(x) for x in input().split()]
    cards = [int(x) for x in input().split()]
    return n, k, cards


def count_of_results(n, k, cards: list[int]):
    card_to_count = defaultdict(int)
    for card in cards:
        card_to_count[card] += 1
    unique_cards = sorted(card_to_count.keys())
    r = 0
    count = 0
    dups = 0
    for l in range(len(unique_cards)):
        while r < len(unique_cards) and unique_cards[r] <= unique_cards[l] * k:
            if card_to_count[unique_cards[r]] >= 2:
                dups += 1
            r += 1
        range_length = r - l
        if card_to_count[unique_cards[l]] >= 2:
            count += (range_length - 1) * 3
        if card_to_count[unique_cards[l]] >= 3:
            count += 1
        count += (range_length - 1) * (range_length - 2) * 3
        if card_to_count[unique_cards[l]] >= 2:
            dups -= 1
        count += dups * 3
    return count


def main():
    print(count_of_results(*read_input()))


if __name__ == '__main__':
    main()
