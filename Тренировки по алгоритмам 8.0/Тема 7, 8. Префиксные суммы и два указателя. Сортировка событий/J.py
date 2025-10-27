EPS = 10 ** -9
CRASH = 0
WALL = 1
FINISH = 2


def motorsport(n: int, l: int, w: int, cars: list[tuple[int, int, int, int]]):
    events = []
    for i, (x, y, vx, vy) in enumerate(cars):
        if vx > 0:
            t_f = (l - x) / vx
            events.append((t_f, FINISH, i))
        if vy == 0:
            continue
        t_w = (w - y) / vy if vy > 0 else -y / vy
        events.append((t_w, WALL, i))

    for i in range(n - 1):
        xi, yi, vxi, vyi = cars[i]
        for j in range(i + 1, n):
            xj, yj, vxj, vyj = cars[j]
            dx, dy = xi - xj, yi - yj
            dvx, dvy = vxi - vxj, vyi - vyj
            if dvx == dvy == 0:
                continue
            if dvx == 0:
                if dx == 0:
                    t_crash = -dy / dvy
                    if t_crash > 0:
                        events.append((t_crash, CRASH, (i, j)))
            elif dvy == 0:
                if dy == 0:
                    t_crash = -dx / dvx
                    if t_crash > 0:
                        events.append((t_crash, CRASH, (i, j)))
            else:
                tx = -dx / dvx
                ty = -dy / dvy
                if tx > 0 and ty > 0 and abs(tx - ty) < EPS:
                    t_crash = tx
                    events.append((t_crash, CRASH, (i, j)))
    events.sort()
    crashed = dict()
    cars_finished = []
    finish_t = None
    for t, event, car in events:
        if event == WALL:
            crashed[car] = t
        elif event == CRASH:
            car_i, car_j = car
            if car_i not in crashed and car_j not in crashed:
                crashed[car_i] = t
                crashed[car_j] = t
            elif car_i in crashed and abs(t - crashed[car_i]) < EPS:
                crashed[car_j] = t
            elif car_j in crashed and abs(t - crashed[car_j]) < EPS:
                crashed[car_i] = t
        elif event == FINISH:
            if car in crashed:
                continue
            if finish_t is None:
                finish_t = t
            if abs(t - finish_t) < EPS:
                cars_finished.append(car + 1)
    cars_finished.sort()
    return cars_finished


def main():
    n, l, w = map(int, input().split())
    cars = []
    for _ in range(n):
        cars.append(tuple(map(int, input().split())))
    ans = motorsport(n, l, w, cars)
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
