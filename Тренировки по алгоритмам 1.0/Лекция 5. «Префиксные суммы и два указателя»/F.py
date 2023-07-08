def read_input():
    n = int(input())
    rooms = [int(x) for x in input().split()]
    m = int(input())
    conditioners = [tuple([int(x) for x in input().split()]) for _ in range(m)]
    return n, m, rooms, conditioners


def min_cost(n, m, rooms: list[int], conditioners: list[tuple]):
    rooms.sort()
    conditioners.sort(key=lambda t: (t[1], t[0]))
    room_i = cond_i = 0
    cost = 0
    while room_i < n:
        while conditioners[cond_i][0] < rooms[room_i]:
            cond_i += 1
        while room_i < n and conditioners[cond_i][0] >= rooms[room_i]:
            cost += conditioners[cond_i][1]
            room_i += 1
    return cost


def main():
    print(min_cost(*read_input()))


if __name__ == '__main__':
    main()
