def input_read():
    n = int(input().strip())
    requests = [input().strip() for _ in range(n)]
    return n, requests


class MyStack:
    def __init__(self):
        self.pref_sums = [0]
        self.stack = []

    def top_n(self, n: int):
        if not self.stack or len(self.stack) < n:
            raise RuntimeError("Empty")
        return self.pref_sums[-1] - self.pref_sums[len(self.stack) - n]

    def push(self, item):
        self.stack.append(item)
        self.pref_sums.append(self.pref_sums[-1] + item)

    def pop(self):
        self.pref_sums.pop()
        return self.stack.pop()

    def __repr__(self):
        return f'{str(self.stack)} {str(self.pref_sums)}'


def stack_with_sum(n, requests):
    stack = MyStack()
    for request in requests:
        match request[0]:
            case '+':
                stack.push(int(request[1:]))
            case '-':
                print(stack.pop())
            case '?':
                print(stack.top_n(int(request[1:])))


def main():
    stack_with_sum(*input_read())


if __name__ == '__main__':
    main()
