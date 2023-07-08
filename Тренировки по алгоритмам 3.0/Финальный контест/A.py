from collections import defaultdict

products = defaultdict(int)


def main():
    n = int(input())
    train = []
    for _ in range(n):
        commands = input().split()
        cmd = commands[0]
        if cmd == 'add':
            count = int(commands[1])
            product = commands[2]
            products[product] += count
            train.append((product, count))
        elif cmd == 'get':
            product = commands[1]
            print(products[product])
        elif cmd == 'delete':
            wagons_count = int(commands[1])
            wagons_popped = 0
            product = ''
            while wagons_popped < wagons_count:
                product, wagons = train.pop()
                wagons_popped += wagons
                products[product] -= wagons
            if wagons_popped != wagons_count:
                products[product] += wagons_popped - wagons_count
                train.append((product, wagons_popped - wagons_count))


if __name__ == '__main__':
    main()
