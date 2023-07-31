def read_input():
    n, m = [int(x) for x in input().split()]
    bodies = [i for i in range(n + 1)]
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        bodies[a], bodies[b] = bodies[b], bodies[a]
    return n, bodies


def swap(bodies: list[int], a: int, b: int) -> int:
    print(a, b)
    bodies[a], bodies[b] = bodies[b], bodies[a]
    return bodies[b]


def futurama(n: int, bodies: list[int]):
    for i in range(1, n - 1):
        if bodies[i] != i:
            now = i
            while bodies[now] != i:
                now = swap(bodies, now, n - 1)
            now = swap(bodies, now, n)
            now = swap(bodies, now, n)
            swap(bodies, bodies[n - 1], n - 1)
    if bodies[n] != n:
        swap(bodies, n - 1, n)


def main():
    futurama(*read_input())


if __name__ == '__main__':
    main()
