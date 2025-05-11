def read_input():
    n = int(input().strip())
    requests = []
    while line := input():
        if line == 'HELP':
            break
        requests.append(line)
    return n, requests


def guess_number2(n: int, requests: list[str]):
    initial = {i for i in range(1, n + 1)}
    for request in requests:
        req_set = set(map(int, request.split()))
        intersected = initial.intersection(req_set)
        if len(initial) < len(intersected) * 2:
            print('YES')
            initial = intersected
        else:
            print('NO')
            initial.difference_update(intersected)
    print(*sorted(initial))


def main():
    guess_number2(*read_input())


if __name__ == '__main__':
    main()
