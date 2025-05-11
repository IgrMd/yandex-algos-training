def read_input():
    n, k = map(int, input().split())
    requests = []
    for _ in range(k):
        a, b = map(int, input().split())
        requests.append((a, b))
    return n, k, requests


def strikes(n: int, k: int, requests: list[str]):
    weekends = set()
    for weekend in range(6, n + 1, 7):
        weekends.add(weekend)
        weekends.add(weekend + 1)
    ans = set()
    for a, b in requests:
        for day in range(a, n + 1, b):
            if day in weekends:
                continue
            ans.add(day)
    return len(ans)


def main():
    print(strikes(*read_input()))


if __name__ == '__main__':
    main()
