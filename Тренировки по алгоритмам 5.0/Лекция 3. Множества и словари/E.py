def read_input():
    sets = []
    for _ in range(3):
        n1 = int(input())
        sets.append(set(map(int, input().split())))
    return sets


def two_of_three(sets: list[set]):
    ans = sets[0].intersection(sets[1])
    ans.update(sets[1].intersection(sets[2]))
    ans.update(sets[0].intersection(sets[2]))
    return sorted(ans)


def main():
    print(*two_of_three(read_input()), sep=' ')


if __name__ == '__main__':
    main()
