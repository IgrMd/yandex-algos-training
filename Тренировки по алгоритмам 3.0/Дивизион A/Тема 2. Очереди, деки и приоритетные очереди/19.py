from heapq import heapify, heappush, heappop


def read_input():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    return n, numbers


def get_cost(n, numbers):
    heapify(numbers)
    total_cost = 0
    while len(numbers):
        summ = heappop(numbers)
        if not len(numbers):
            return total_cost
        summ += heappop(numbers)
        total_cost += summ * 0.05
        heappush(numbers, summ)
def main():
    print(f'{get_cost(*read_input()):.2f}')


if __name__ == '__main__':
    main()
