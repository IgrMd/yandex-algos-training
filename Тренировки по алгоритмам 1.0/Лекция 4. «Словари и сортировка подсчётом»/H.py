def read_input():
    g, s = [int(x) for x in input().split()]
    word = input()
    sequence = input()
    return g, s, word, sequence


def maya(g, s, word, sequence):
    di = ord('A')
    word_array = [0] * (ord('z') - di + 1)
    sub_str_arr = [0] * (ord('z') - di + 1)

    for i, c in enumerate(word):
        word_array[ord(c) - di] += 1
        sub_str_arr[ord(sequence[i]) - di] += 1
    answer = int(sub_str_arr == word_array)
    i = 0
    j = i + g
    while j < s:
        sub_str_arr[ord(sequence[i]) - di] -= 1
        sub_str_arr[ord(sequence[j]) - di] += 1
        if word_array == sub_str_arr:
            answer += 1
        i += 1
        j += 1
    return answer


def main():
    print(maya(*read_input()))


if __name__ == '__main__':
    main()
