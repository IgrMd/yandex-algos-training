def read_input():
    n = int(input())
    sequence = [int(x) for x in input().split()]
    return n, sequence


def sub_sequence(n, sequence):
    dp = [1] * n
    prev = [-1] * n
    dp[0] = 1
    prev[0] = -1
    for i in range(1, n):
        j = i
        j_max_seq = j
        max_seq_count = 0
        while j >= 0:
            if sequence[j] < sequence[i] and dp[j] > max_seq_count:
                j_max_seq = j
                max_seq_count = dp[j]
            j -= 1

        if j_max_seq != i:
            dp[i] += dp[j_max_seq]
            prev[i] = j_max_seq

    max_i = 0
    for i in range(n):
        if dp[i] > dp[max_i]:
            max_i = i
    answ = [sequence[max_i]]
    i_prev = prev[max_i]
    while i_prev != -1:
        answ.append(sequence[i_prev])
        i_prev = prev[i_prev]
    return answ

def main():
    print(*sub_sequence(*read_input())[::-1])


if __name__ == '__main__':
    main()
