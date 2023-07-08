def read_input():
    index_to_cmd = {0: 'N', 1: 'S', 2: 'W', 3: 'E', 4: 'U', 5: 'D'}
    cmd_to_index = dict(map(lambda item: (item[1], item[0]), index_to_cmd.items()))
    commands = dict()
    for i in index_to_cmd:
        commands[index_to_cmd[i]] = input()
    cmd, param = input().split()
    param = int(param)
    return cmd, param, commands, index_to_cmd, cmd_to_index


def movements_dp(command, param, commands, index_to_cmd, cmd_to_index):
    dp = [[0] * (param + 1) for _ in range(6)]
    for line in dp:
        line[1] = 1
    for j in range(2, param + 1):
        for i in range(6):
            dp[i][j] = 1
            for cmd in commands[index_to_cmd[i]]:
                dp[i][j] += dp[cmd_to_index[cmd]][j - 1]
    return dp[cmd_to_index[command]][param]


def main():
    print(movements_dp(*read_input()))


if __name__ == '__main__':
    main()
