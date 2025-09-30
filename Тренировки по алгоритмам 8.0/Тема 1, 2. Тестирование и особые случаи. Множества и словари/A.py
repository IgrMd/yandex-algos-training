def read_input():
    n = int(input())
    mushrooms = [int(i) for i in input().split()]
    return n, mushrooms


def split_mushrooms(n, mushrooms):
    v_mushrooms = list(mushrooms[::2])
    m_mushrooms = list(mushrooms[1::2])
    answer = sum(v_mushrooms) - sum(m_mushrooms)
    v_min = min(v_mushrooms)
    m_max = max(m_mushrooms)
    if m_max > v_min:
        answer -= 2 * v_min
        answer += 2 * m_max
    return answer


def main():
    print(split_mushrooms(*read_input()))


if __name__ == '__main__':
    main()
