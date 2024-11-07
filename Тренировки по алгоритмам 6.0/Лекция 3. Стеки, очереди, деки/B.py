def input_read():
    n = int(input())
    costs = [int(x) for x in input().split()]
    return n, costs


def get_town_indexes(n, costs):
    no_answer = []
    answer = [-1] * n
    for i, cost in enumerate(costs):
        if len(no_answer) == 0:
            no_answer.append([i, cost])
            continue
        while len(no_answer) and cost < no_answer[-1][1]:
            no_answer_i, no_answer_cost = no_answer.pop()
            answer[no_answer_i] = i
        no_answer.append([i, cost])
    return answer


def main():
    print(*get_town_indexes(*input_read()))


if __name__ == '__main__':
    main()
