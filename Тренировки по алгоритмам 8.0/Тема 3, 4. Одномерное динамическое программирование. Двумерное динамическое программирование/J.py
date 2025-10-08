import sys


def read_input():
    N, L = map(int, input().split())
    shops = [list(map(int, input().split())) for _ in range(N)]
    return N, L, shops


P = 0  # standard price
R = 1  # discount threshold
Q = 2  # discount price
F = 3  # available amount
INF = float('inf')


def masquerade(N, L, shops: list[list]):
    L_max = L + max(shops, key=lambda x: x[F])[F]
    dp_costs = [[INF] * N for _ in range(L_max)]
    dp_count = [[INF] * N for _ in range(L_max)]

    def cost(t, i):
        if t > shops[i][F]:
            return INF
        return t * (shops[i][P] if t < shops[i][R] else shops[i][Q])

    for l in range(L_max):
        dp_costs[l][0] = cost(l, 0)
        if dp_costs[l][0] == INF:
            break
        dp_count[l][0] = l
    for l in range(L_max):
        for i in range(1, N):
            mem_c = dp_costs[l][i]
            mem_t = 0
            for t in range(l + 1):
                c = cost(t, i) + dp_costs[l - t][i - 1]
                if c < mem_c:
                    mem_c = c
                    mem_t = t
            dp_costs[l][i] = mem_c
            dp_count[l][i] = mem_t
    l_left = L_max
    min_cost = INF
    for l in range(L, L_max):
        for i in range(N):
            if dp_costs[l][i] < min_cost:
                l_left = l
                min_cost = dp_costs[l][i]
    if min_cost == INF:
        return -1, []
    ans = []
    for i in range(N - 1, -1, -1):
        ans.append(dp_count[l_left][i])
        l_left -= dp_count[l_left][i]
    ans.reverse()
    return min_cost, ans


def tests():
    for i in range(1, 28):
        with open(f'./.tests/Input{i:02d}.txt', 'r') as f:
            sys.stdin = f
            N, L, shops = read_input()
        with open(f'./.tests/Answer{i:02d}.txt', 'r') as f:
            sys.stdin = f
            correct_ans = int(input().strip())

        def cost(t, i):
            if t > shops[i][F]:
                return INF
            return t * (shops[i][P] if t < shops[i][R] else shops[i][Q])

        ans, arr = masquerade(N, L, shops)
        if ans != correct_ans:
            assert ans == correct_ans
        if ans == -1:
            continue
        validate = 0
        for i, t in enumerate(arr):
            validate += cost(t, i)
        if validate != correct_ans:
            assert validate == correct_ans
        sys.stdin = sys.__stdin__


def main():
    ans, arr = masquerade(*read_input())
    print(ans)
    print(*arr)


if __name__ == '__main__':
    # tests()
    main()
