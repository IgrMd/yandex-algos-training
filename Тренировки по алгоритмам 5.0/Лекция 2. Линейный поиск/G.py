def read_input():
    t = int(input())
    arrays = []
    for _ in range(t):
        n = int(input())
        arrays.append(list(map(int, input().split())))
    return arrays


def execute(arrays: list[list]):
    for arr in arrays:
        ans = []
        local_min = arr[0]
        local_len = 1
        for i in range(1, len(arr)):
            if local_len < arr[i]:
                if local_len < local_min:
                    local_len += 1
                    local_min = min(local_min, arr[i])
                else:
                    ans.append(local_len)
                    local_min = arr[i]
                    local_len = 1
            else:
                ans.append(local_len)
                local_min = arr[i]
                local_len = 1
        ans.append(local_len)
        print(len(ans))
        print(*ans, sep=' ')


def main():
    execute(read_input())


if __name__ == '__main__':
    main()
