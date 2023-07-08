class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __hash__(self):
        return self.x + 63 * self.y

    def sq_vector_len(self):
        return self.x ** 2 + self.y ** 2


def read_input():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        points.append(Point(x, y))
    return n, points


def triangles(n, points: list[Point]):
    count = 0
    for i, now_point in enumerate(points):
        neibs_len = []
        vectors_used = set()
        for j, neib_point in enumerate(points):
            vector = now_point - neib_point
            if Point(-vector.x, -vector.y) in vectors_used:
                count -= 1
            vectors_used.add(vector)
            neibs_len.append(vector.sq_vector_len())
        neibs_len.sort()
        r = 0
        for l in range(len(neibs_len)):
            while r < len(neibs_len) and neibs_len[r] == neibs_len[l]:
                r += 1
            count += r - l - 1

    return count


def main():
    print(triangles(*read_input()))


if __name__ == '__main__':
    main()
