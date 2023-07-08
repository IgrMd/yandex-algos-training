def read_input():
    lst = input().split()
    k = int(lst[0])
    containers = [float(x) for x in lst[1:]]
    return k, containers


def is_possible_to_sort(k, containers):
    if len(containers) == 1:
        return 1
    answer = []
    bottom = []
    bottom.append(containers[0])
    for i in range(1, len(containers)):
        while len(bottom) and bottom[-1] < containers[i]:
            answer.append(bottom.pop())
        bottom.append(containers[i])

    while len(bottom):
        answer.append(bottom.pop())
    for i in range(1, len(answer)):
        if answer[i - 1] > answer[i]:
            return 0
    return 1


def main():
    n = int(input())
    for i in range(n):
        print(is_possible_to_sort(*read_input()))


if __name__ == '__main__':
    main()
