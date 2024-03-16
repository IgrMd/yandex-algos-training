from dataclasses import dataclass, field
from collections import defaultdict, deque


def read_input():
    requests = deque()
    while True:
        request = input().strip()
        if not len(request):
            break
        requests.append(request)
    # with open('input.txt', 'r') as fp:
    #     for line in fp:
    #         requests.append(line.strip())
    return requests


@dataclass
class PlayerInfo:
    team: str = ''
    goals_count: int = 0
    open_score: int = 0
    goals_per_minute: list[int] = field(default_factory=lambda: [0] * 91)


@dataclass
class TeamInfo:
    goals_count: int = 0
    games_count: int = 0
    open_score: int = 0


def handle_request(request: str, teams: dict[str: TeamInfo], players: dict[str: PlayerInfo()]):
    tokens = request.split()
    if request.startswith('Total goals for'):
        team = ' '.join(tokens[3:])
        print(teams[team].goals_count)
    elif request.startswith('Mean goals per game for'):
        team = ' '.join(tokens[5:])
        print(teams[team].goals_count / teams[team].games_count)
    elif request.startswith('Total goals by'):
        player = ' '.join(tokens[3:])
        print(players[player].goals_count)
    elif request.startswith('Mean goals per game by'):
        player = ' '.join(tokens[5:])
        print(players[player].goals_count / teams[players[player].team].games_count)
    elif request.startswith('Goals on minute'):
        minute = int(tokens[3])
        player = ' '.join(tokens[5:])
        print(players[player].goals_per_minute[minute])
    elif request.startswith('Goals on first'):
        minute = int(tokens[3])
        player = ' '.join(tokens[6:])
        print(sum(players[player].goals_per_minute[:minute + 1]))
    elif request.startswith('Goals on last'):
        minute = int(tokens[3])
        player = ' '.join(tokens[6:])
        print(sum(players[player].goals_per_minute[91 - minute:]))
    elif request.startswith('Score opens by'):
        if request.count('"'):
            team = ' '.join(tokens[3:])
            print(teams[team].open_score)
        else:
            player = ' '.join(tokens[3:])
            print(players[player].open_score)
    elif request.startswith('"'):
        i = tokens.index('-')
        team1 = ' '.join(tokens[:i])
        team2 = ' '.join(tokens[i + 1:-1])
        score1, score2 = map(int, tokens[-1].split(sep=':'))
        return team1, team2, score1, score2
    return None


def football(requests: deque):
    teams = defaultdict(lambda: TeamInfo())
    players = defaultdict(lambda: PlayerInfo())
    while len(requests):
        request = requests.popleft()
        result = handle_request(request, teams, players)
        if result:
            team1, team2, score1, score2 = result
            t1, pl1 = handle_game_results(teams, players, requests, score1, team1)
            t2, pl2 = handle_game_results(teams, players, requests, score2, team2)
            if t1 < t2:
                players[pl1].open_score += 1
                teams[team1].open_score += 1
            elif t2 < t1:
                players[pl2].open_score += 1
                teams[team2].open_score += 1
            else:
                pass


def handle_game_results(teams, players, requests, score, team):
    teams[team].goals_count += score
    teams[team].games_count += 1
    first_goal, first_player = 91, ''
    for _ in range(score):
        tokens = requests.popleft().split()
        player = ' '.join(tokens[:-1])
        minute = int(tokens[-1][:-1])
        players[player].team = team
        players[player].goals_count += 1
        players[player].goals_per_minute[minute] += 1
        if minute < first_goal:
            first_goal = minute
            first_player = player
    return first_goal, first_player


def main():
    football(read_input())


if __name__ == '__main__':
    main()
