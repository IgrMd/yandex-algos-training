def input_read():
    first = [int(x) for x in input().split()]
    second = [int(x) for x in input().split()]
    return first, second


def play(first: list, second: list):
    step = 0
    while step <= 10e6 and len(first) and len(second):
        step += 1
        first_card = first.pop(0)
        second_card = second.pop(0)
        if first_card == 0 and second_card == 9:
            first.append(first_card)
            first.append(second_card)
            continue
        if second_card == 0 and first_card == 9:
            second.append(first_card)
            second.append(second_card)
            continue
        if first_card > second_card:
            first.append(first_card)
            first.append(second_card)
        else:
            second.append(first_card)
            second.append(second_card)
    if not len(first):
        print(f'second {step}')
    elif not len(second):
        print(f'first {step}')
    else:
     print('botva')


def main():
    play(*input_read())


if __name__ == '__main__':
    main()
