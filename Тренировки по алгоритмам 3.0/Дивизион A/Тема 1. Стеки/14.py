def read_input():
    heights = [int(x) for x in input().split()]
    n = heights.pop(0)
    return n, heights


def get_max_square(n, heights):
    no_answer = []
    min_r = [len(heights)] * n
    for i, height in enumerate(heights):
        if len(no_answer) == 0:
            no_answer.append([i, height])
            continue
        while len(no_answer) and height < no_answer[-1][1]:
            no_answer_i, no_answer_height = no_answer.pop()
            min_r[no_answer_i] = i
        no_answer.append([i, height])

    no_answer.clear()
    min_l = [-1] * n
    for i in reversed(range(len(heights))):
        height = heights[i]
        if len(no_answer) == 0:
            no_answer.append([i, height])
            continue
        while len(no_answer) and height < no_answer[-1][1]:
            no_answer_i, no_answer_height = no_answer.pop()
            min_l[no_answer_i] = i
        no_answer.append([i, height])

    max_square = 0
    for i, height in enumerate(heights):
        square = height * (min_r[i] - min_l[i] - 1)
        max_square = max(max_square, square)
    return max_square


def main():
    print(get_max_square(*read_input()))


if __name__ == '__main__':
    main()
