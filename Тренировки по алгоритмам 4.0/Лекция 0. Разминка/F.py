def read_input():
    k = int(input().strip())
    n = int(input().strip())
    floor_people = [0]
    for _ in range(n):
        floor_people.append(int(input().strip()))
    return k, n, floor_people


def elevator(k, n, floor_people):
    min_time = 0
    parking = 0
    curr_elevator_floor = parking
    for floor in range(n, parking, -1):
        if floor_people[floor] == 0:
            continue
        min_time += abs(floor - curr_elevator_floor)
        curr_elevator_floor = floor
        rest = floor_people[floor] % k
        full_load_count = floor_people[floor] // k
        if full_load_count:
            min_time += (full_load_count * 2 - 1) * (floor - parking)
            floor_people[floor] -= full_load_count * k
            floor_people[parking] += full_load_count * k
            curr_elevator_floor = parking
        if rest:
            min_time += abs(floor - curr_elevator_floor)
            floor_people[floor - 1] += rest
            floor_people[floor] = 0
            min_time += 1
            curr_elevator_floor = floor - 1
    return min_time


def main():
    print(elevator(*read_input()))


if __name__ == '__main__':
    main()
