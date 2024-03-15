def read_input():
    n = int(input())
    playlists = []
    min_index, min_count = 0, 10 ** 7
    for i in range(n):
        k = int(input())
        if min_count < k:
            min_index, min_count = i, k
        playlist = set(input().split())
        playlists.append(playlist)
    return min_index, playlists


def best_playlist(min_index: int, playlists: list[set]):
    ans = []
    for song in playlists[min_index]:
        flag = True
        for playlist in playlists:
            if song not in playlist:
                flag = False
                break
        if flag:
            ans.append(song)
    ans.sort()
    return ans


def main():
    ans = best_playlist(*read_input())
    print(len(ans))
    print(*ans, sep=' ')


if __name__ == '__main__':
    main()
