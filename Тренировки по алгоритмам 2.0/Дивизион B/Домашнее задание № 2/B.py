def read_input():
    buildings = [int(x) for x in input().split()]
    return buildings


INF = 10 ** 6


def max_path(buildings: list[int]):
    prev_store_ndex = -INF
    answer = -INF
    for i in range(len(buildings)):
        building = buildings[i]
        match building:
            case 0:
                continue
            case 1:
                next_store_index = i
                while next_store_index < len(buildings) and buildings[next_store_index] != 2:
                    next_store_index += 1
                if next_store_index >= len(buildings):
                    next_store_index = INF
                answer = max(answer, min(i - prev_store_ndex, next_store_index - i))
            case 2:
                prev_store_ndex = i
    return answer


def main():
    print(max_path(read_input()))


if __name__ == '__main__':
    main()
