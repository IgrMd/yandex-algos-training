from heapq import heappop, heappush


class Helper:
    def __init__(self, t, z, y, helper_id):
        self.t, self.z, self.y, self.id = t, z, y, helper_id

    def __repr__(self):
        return f't: {self.t}, z: {self.z}, y: {self.y}, id: {self.id}'


def read_input():
    m, n = [int(x) for x in input().split()]
    helpers_data = []
    for helper_id in range(n):
        t, z, y = [int(x) for x in input().split()]
        helpers_data.append(Helper(t, z, y, helper_id))
    return n, m, helpers_data


def helpers(n: int, m: int, helpers_data: list[Helper], ):
    heap = []
    now_time = 0
    for helper in helpers_data:
        heappush(heap, (now_time + helper.t, helper.id))
    helper_to_balloons = [0] * n
    while m > 0:
        now_time, helper_id = heappop(heap)
        helper_to_balloons[helper_id] += 1
        if helper_to_balloons[helper_id] % helpers_data[helper_id].z == 0:
            heappush(heap, (now_time + helpers_data[helper_id].t + helpers_data[helper_id].y, helper_id))
        else:
            heappush(heap, (now_time + helpers_data[helper_id].t, helper_id))
        m -= 1
    return now_time, helper_to_balloons


def main():
    now_time, helper_to_balloons = helpers(*read_input())
    print(now_time)
    print(*helper_to_balloons)


if __name__ == '__main__':
    main()
