from collections import defaultdict
import sys


def read_input():
    db = defaultdict(lambda: defaultdict(int))
    for line in sys.stdin.readlines():
        customer, product, count = line.split()
        db[customer][product] += int(count)
    return db


def print_db(db: dict[dict[int]]):
    for customer, products in sorted(db.items()):
        print(f'{customer}:')
        for product, count in sorted(products.items()):
            print(f'{product} {count}')


def main():
    print_db(read_input())


if __name__ == '__main__':
    main()
