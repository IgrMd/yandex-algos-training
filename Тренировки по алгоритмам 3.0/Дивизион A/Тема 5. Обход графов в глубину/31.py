def read_input():
    n = int(input())
    labyrinth = [input() for _ in range(n)]
    x, y = [int(char) for char in input().split()]
    return n, labyrinth, x, y


def dfs(graph, visited, now):
    visited[now] = 1
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v)


def room_square(n, labyrinth, x, y):
    i_neibs = [-1, 1, 0, 0]
    j_neibs = [0, 0, -1, 1]
    graph = [list() for _ in range(n ** 2)]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            for k in range(4):
                i_neib = i + i_neibs[k]
                j_neib = j + j_neibs[k]
                c1 = labyrinth[i][j]
                c2 = labyrinth[i_neib][j_neib]
                if c1 == c2 == '.':
                    graph[i + j * (n - 1)].append(i_neib + j_neib * (n - 1))
    visited = [0] * (n ** 2)
    dfs(graph, visited, x - 1 + (y - 1) * (n - 1))
    return sum(visited)

l1 = ['***', '*.*', '***']
l2 = ['*****', '*...*', '***.*', '*...*', '*****']

assert room_square(3, l1, 2, 2) == 1
assert room_square(5, l2, 2, 2) == 7


def main():
    print(room_square(*read_input()))


if __name__ == '__main__':
    main()
