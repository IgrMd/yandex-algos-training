def normalized(phone: str):
    for c in '()-':
        phone = phone.replace(c, '')
    phone = phone.replace('+7', '8')
    if len(phone) == 7:
        return '495', phone
    else:
        return phone[1:4], phone[4:]


def main():
    target = input()
    phones = [input() for i in range(3)]
    target = normalized(target)
    for phone in phones:
        if target == normalized(phone):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
