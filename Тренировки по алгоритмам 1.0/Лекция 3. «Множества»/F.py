from collections import defaultdict


def read_input():
    gen1 = input()
    gen2 = input()
    return gen1, gen2


def get_pairs(gen: str) -> dict[int]:
    pairs = defaultdict(int)
    for i in range(len(gen) - 1):
        pairs[gen[i:i + 2]] += 1
    return pairs


def genomes(gen1, gen2):
    pairs1 = get_pairs(gen1)
    pairs2 = get_pairs(gen2)

    answer = 0
    for pair, num in pairs1.items():
        if pair in pairs2:
            answer += num

    return answer


def main():
    print(genomes(*read_input()))


if __name__ == '__main__':
    main()
