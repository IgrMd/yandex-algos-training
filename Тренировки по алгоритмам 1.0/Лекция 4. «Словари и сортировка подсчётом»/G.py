from collections import defaultdict
import sys


def read_input():
    requests = sys.stdin.readlines()
    return requests


def deposit(bank: dict[str:int], request: list[str]):
    bank[request[1]] += int(request[2])


def withdraw(bank: dict[str:int], request: list[str]):
    bank[request[1]] -= int(request[2])


def balance(bank: dict[str:int], request: list[str]):
    if request[1] in bank:
        print(bank[request[1]])
    else:
        print('ERROR')


def transfer(bank: dict[str:int], request: list[str]):
    amount = int(request[3])
    bank[request[1]] -= amount
    bank[request[2]] += amount


def income(bank: dict[str:int], request: list[str]):
    p = int(request[1])
    for client, bill in bank.items():
        if bill > 0:
            bank[client] += int(bill * p / 100)


def proceed(requests: list[str]):
    bank = defaultdict(int)
    actions = {'DEPOSIT': deposit,
               'WITHDRAW': withdraw,
               'BALANCE': balance,
               'TRANSFER': transfer,
               'INCOME': income}
    for request in requests:
        request = request.split()
        actions[request[0]](bank, request)


def main():
    proceed(read_input())


if __name__ == '__main__':
    main()
