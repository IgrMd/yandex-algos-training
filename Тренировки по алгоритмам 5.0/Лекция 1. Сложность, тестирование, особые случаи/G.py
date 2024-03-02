import sys

sys.setrecursionlimit(10000)

HIT_BARRACKS = True
HIT_ARMY = False


def read_input():
    x = int(input())
    y = int(input())
    p = int(input())
    return x, y, p


def try_step(curr_step,
             target,
             barrack_health,
             my_soldiers,
             enemy_soldiers, p):
    if my_soldiers <= 0:
        return -1
    if barrack_health <= 0 and enemy_soldiers <= 0:
        return curr_step
    available_solders = my_soldiers
    if target == HIT_BARRACKS:
        if available_solders > barrack_health:
            available_solders -= barrack_health
            barrack_health = 0
        else:
            barrack_health -= available_solders
            available_solders = 0
        enemy_soldiers = max(0, enemy_soldiers - available_solders)
    elif target == HIT_ARMY:
        if my_soldiers == enemy_soldiers:
            if barrack_health and p >= my_soldiers:
                return -1
        if available_solders > enemy_soldiers:
            available_solders -= enemy_soldiers
            enemy_soldiers = 0
        else:
            enemy_soldiers -= available_solders
            available_solders = 0
        barrack_health = max(0, barrack_health - available_solders)
    my_soldiers -= enemy_soldiers
    if barrack_health:
        enemy_soldiers += p
    if barrack_health >= my_soldiers and p == my_soldiers:
        return -1
    step_cnt1 = -1
    if not enemy_soldiers or barrack_health <= my_soldiers:
        step_cnt1 = try_step(curr_step + 1, HIT_BARRACKS, barrack_health, my_soldiers, enemy_soldiers, p)
    step_cnt2 = try_step(curr_step + 1, HIT_ARMY, barrack_health, my_soldiers, enemy_soldiers, p)
    if step_cnt1 != -1 and step_cnt2 != -1:
        return min(step_cnt1, step_cnt2)
    if step_cnt1 == -1:
        return step_cnt2
    if step_cnt2 == -1:
        return step_cnt1
    return -1


def destroy_barracks(x, y, p):
    my_soldiers = x
    barrack_health = y
    enemy_soldiers = 0
    step_cnt1 = try_step(0, HIT_BARRACKS, barrack_health, my_soldiers, enemy_soldiers, p)
    step_cnt2 = try_step(0, HIT_ARMY, barrack_health, my_soldiers, enemy_soldiers, p)
    if step_cnt1 != -1 and step_cnt2 != -1:
        return min(step_cnt1, step_cnt2)
    if step_cnt1 == -1:
        return step_cnt2
    if step_cnt2 == -1:
        return step_cnt1
    return -1


assert destroy_barracks(9, 427, 1) == 54
assert destroy_barracks(499, 500, 499) == 3
assert destroy_barracks(250, 500, 208) == 5
assert destroy_barracks(250, 500, 187) == 4
assert destroy_barracks(10, 11, 15) == 4
assert destroy_barracks(1, 2, 1) == -1
assert destroy_barracks(1, 1, 1) == 1
assert destroy_barracks(25, 200, 10) == 13


def main():
    print(destroy_barracks(*read_input()))


if __name__ == '__main__':
    main()
