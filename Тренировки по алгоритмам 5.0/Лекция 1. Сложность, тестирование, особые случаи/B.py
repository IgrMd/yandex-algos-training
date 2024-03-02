def read_input():
    first_game = [int(x) for x in input().split(sep=':')]
    curr_game = [int(x) for x in input().split(sep=':')]
    first_game_place = int(input())
    return first_game, curr_game, first_game_place


def goals_to_win(first_game, curr_game, first_game_place):
    first_team_goals = first_game[0] + curr_game[0]
    second_team_goals = first_game[1] + curr_game[1]
    if first_team_goals > second_team_goals:
        return 0
    goals_to_draw = second_team_goals - first_team_goals
    curr_game[0] += goals_to_draw
    match first_game_place:
        case 1:  # HOME
            if curr_game[0] > first_game[1]:
                return goals_to_draw
            else:
                return goals_to_draw + 1
        case 2:  # GUEST
            if first_game[0] > curr_game[1]:
                return goals_to_draw
            else:
                return goals_to_draw + 1
    return 0


def main():
    print(goals_to_win(*read_input()))


if __name__ == '__main__':
    main()
