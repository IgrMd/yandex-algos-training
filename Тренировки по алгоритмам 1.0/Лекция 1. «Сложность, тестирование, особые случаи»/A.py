def read_input():
    begin, end = tuple(map(int, input().split()))
    regim = input()
    return begin, end, regim


def conditioner(begin, end, regim):
    if regim == 'fan':
        return begin
    if regim == 'auto':
        return end
    if regim == 'freeze':
        return end if end < begin else begin
    if regim == 'heat':
        return end if begin < end else begin


def main():
    print(conditioner(*read_input()))


if __name__ == '__main__':
    main()
