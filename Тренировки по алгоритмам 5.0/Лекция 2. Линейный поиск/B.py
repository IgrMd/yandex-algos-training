def read_input():
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    return n, k, prices


def max_income(n, k, prices):
    answer = 0
    for i, price in enumerate(prices):
        answer = max(answer, max(prices[i: min(i + k + 1, len(prices))]) - price)
    return answer


def main():
    print(max_income(*read_input()))


if __name__ == '__main__':
    main()
