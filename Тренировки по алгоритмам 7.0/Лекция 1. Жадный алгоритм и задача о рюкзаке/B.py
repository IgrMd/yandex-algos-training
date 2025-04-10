def read_input():
    t = int(input().strip())
    queries = []
    for _ in range(t):
        n = int(input().strip())
        queries.append(list(map(int, input().split())))
    return queries


def handle(query: list[int]):
    cur_min = query[0]
    l = 0
    ans = []
    for r in range(1, len(query)):
        cur_min = min(cur_min, query[r])
        cur_len = r - l + 1
        if cur_min >= cur_len:
            continue
        ans.append(r - l)
        l = r
        cur_min = query[r]
    ans.append(len(query) - l)
    print(len(ans))
    print(*ans)


def no_min_no_max(queries: list[list[int]]):
    for query in queries:
        handle(query)


def main():
    no_min_no_max(read_input())


if __name__ == '__main__':
    main()
