from bisect import bisect_left, bisect_right
from dataclasses import dataclass


def read_input():
    # with open('input.txt', 'r') as f:
    #     n = int(f.readline().strip())
    #     parties = []
    #     for i in range(n):
    #         parties.append(Party(*map(int, f.readline().split()), i))
    n = int(input().strip())
    parties = []
    for i in range(n):
        parties.append(Party(*map(int, input().split()), i))
    return n, parties


@dataclass
class Party:
    v: int
    p: int
    i: int


def upper_bound(l, r, cmp, params):
    party = None
    while l < r:
        mid = (l + r) // 2
        ok, i = cmp(mid, *params)
        if ok:
            party = i
            r = mid
        else:
            l = mid + 1
    ok, i = cmp(l, *params)
    if ok:
        party = i
    else:
        l += 1
    return l, party


def can_party_win(amount, i, n, parties: list[Party], pref_sums: list[int]):
    party = parties[i]
    if amount < party.p:
        return False
    can_by = amount - party.p
    if can_by == 0:
        return i == n - 1 and parties[i - 1].v < party.v
    total_votes = party.v + can_by
    index_to_by = bisect_left(parties, total_votes, lo=0, hi=n, key=lambda x: x.v)
    if index_to_by == n:
        return True
    need_to_by = pref_sums[-1] - pref_sums[index_to_by - 1] - (n - index_to_by) * (total_votes - 1)
    return need_to_by <= can_by


def check(amount, n, parties: list[Party], pref_sums: list[int]):
    for i, party in enumerate(parties):
        if party.p == -1:
            continue
        if can_party_win(amount, i, n, parties, pref_sums):
            return True, i
    return False, None


def elections(n: int, parties: list[Party]):
    if n == 1:
        return parties[0].p, n, [parties[0].v]
    parties.sort(key=lambda x: x.v)
    pref_sums = [0] * n
    max_p, total_votes = 0, 0
    for i in range(n):
        pref_sums[i] = pref_sums[i - 1] + parties[i].v
        total_votes += parties[i].v
        max_p = max(max_p, parties[i].p)
    min_amount, mem_i = upper_bound(0, total_votes + max_p, check, (n, parties, pref_sums))
    src_i = 0
    votes_to_by = min_amount - parties[mem_i].p
    target_votes = votes_to_by + parties[mem_i].v
    for i, party in enumerate(parties):
        if i == mem_i:
            src_i = party.i
            party.v = target_votes
            continue
        if party.v >= target_votes:
            votes_to_by -= (party.v - target_votes + 1)
            party.v = target_votes - 1
    for i, party in enumerate(parties):
        if i == mem_i:
            continue
        delta = min(votes_to_by, party.v)
        party.v -= delta
        votes_to_by -= delta
        if votes_to_by <= 0:
            break
    parties.sort(key=lambda x: x.i)
    return min_amount, src_i + 1, [party.v for party in parties]


if __name__ == '__main__':
    cash, p_number, voices = elections(*read_input())
    print(cash)
    print(p_number)
    print(*voices)
