from dataclasses import dataclass


def read_input():
    n, k = map(int, input().split())
    return n, k


def check(network, k):
    for device in network.devices:
        if device.downloaded_parts_count != k:
            return False
    return True


@dataclass
class Response:
    from_id: int = 0
    to_id: int = 0
    part_id: int = 0


@dataclass
class Request:
    from_id: int = 0
    part_id: int = 0


class Device:
    def __init__(self, id_, network, value=False):
        self.id = id_
        self.is_part_downloaded = [value] * network.capacity
        self.downloaded_parts_count = network.capacity if value else 0
        self.other_id_to_worth = [0] * network.size
        self.network = network
        self.requests = []
        self.time = 0

    def send_request(self):
        if self.downloaded_parts_count == self.network.capacity:
            return
        part_id = self.is_part_downloaded.index(False)
        part_count = self.network.parts_count[part_id]
        for part in range(part_id + 1, self.network.capacity):
            if self.is_part_downloaded[part]:
                continue
            if self.network.parts_count[part] < part_count:
                part_count = self.network.parts_count[part]
                part_id = part
        best_device = self.network.devices[0]
        for device in self.network.devices:
            if (device.is_part_downloaded[part_id] and
                    device.downloaded_parts_count < best_device.downloaded_parts_count):
                best_device = device
        best_device.add_request(self.id, part_id)
        self.time += 1

    def add_request(self, device_id, part_id):
        self.requests.append(Request(device_id, part_id))

    def handle_response(self, device_id, part_id):
        self.is_part_downloaded[part_id] = True
        self.network.parts_count[part_id] += 1
        self.downloaded_parts_count += 1
        self.other_id_to_worth[device_id] += 1

    def handle_requests(self):
        if not len(self.requests):
            return
        best_request = self.requests[0]
        for request in self.requests:
            if self.other_id_to_worth[request.from_id] > self.other_id_to_worth[best_request.from_id]:
                best_request = request
            elif self.other_id_to_worth[request.from_id] == self.other_id_to_worth[best_request.from_id]:
                if (self.network.devices[request.from_id].downloaded_parts_count <
                        self.network.devices[best_request.from_id].downloaded_parts_count):
                    best_request = request
        self.requests.clear()
        self.network.responses.append(Response(self.id, best_request.from_id, best_request.part_id))


class Network:
    def __init__(self, n, k):
        self.devices = list()
        self.parts_count = [1] * k
        self.n = n
        self.k = k
        self.responses = list()

    def handle_responses(self):
        for response in self.responses:
            self.devices[response.to_id].handle_response(response.from_id, response.part_id)
        self.responses.clear()

    def send_requests(self):
        for device in self.devices:
            device.send_request()

    def handle_requests(self):
        for device in self.devices:
            device.handle_requests()


def p2p(n: int, k: int):
    network = Network(n, k)
    network.devices.append(Device(0, network, True))
    for i in range(1, n):
        network.devices.append(Device(i, network))
    while not check(network, k):
        network.send_requests()
        network.handle_requests()
        network.handle_responses()

    ans = []
    for i in range(1, n):
        ans.append(network.devices[i].time)
    return ans


def test():
    assert p2p(5, 4) == [9, 9, 10, 10]
    assert p2p(5, 5) == [10, 11, 11, 14]
    assert p2p(4, 4) == [7, 8, 8]
    assert p2p(4, 10) == [19, 20, 20]


def main():
    test()
    print(*p2p(*read_input()), sep=' ')


if __name__ == '__main__':
    main()
