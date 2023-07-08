def read_input():
    n, m = [int(x) for x in input().split()]
    segments = [sorted([int(x) for x in input().split()]) for _ in range(n)]
    points = [int(x) for x in input().split()]
    return n, m, segments, points


def points_belongs_to_segments(n: int, m: int, segments: list, points: list):
    events = []
    for a, b in segments:
        events.append((a, -1))
        events.append((b, 1))
    for point in points:
        events.append((point, 0))
    events.sort()
    segment_count_on_point = {}
    curr_segments_count = 0
    for event in events:
        match event[1]:
            case -1:
                curr_segments_count += 1
            case 0:
                segment_count_on_point[event[0]] = curr_segments_count
            case 1:
                curr_segments_count -= 1
    answer = []
    for point in points:
        answer.append(segment_count_on_point[point])
    return answer


def main():
    print(*points_belongs_to_segments(*read_input()))


if __name__ == '__main__':
    main()
