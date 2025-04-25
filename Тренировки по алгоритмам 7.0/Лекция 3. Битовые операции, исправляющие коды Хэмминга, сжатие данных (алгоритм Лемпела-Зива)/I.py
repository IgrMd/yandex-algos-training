POW2 = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072}


def encode(s: str):
    encoded = [0]
    encoded_len = 1
    for c in s:
        while encoded_len in POW2:
            encoded.append(1)
            encoded_len += 1
        encoded.append(int(c))
        encoded_len += 1
    ctrl_i = 1
    while ctrl_i < encoded_len:
        for i in range(2, len(encoded)):
            if ctrl_i == i:
                continue
            if ctrl_i & i:
                encoded[ctrl_i] ^= encoded[i]
        ctrl_i = ctrl_i << 1
    for i in range(encoded_len):
        encoded[i] = str(encoded[i])
    return ''.join(encoded[1:])


def decode(s: str):
    encoded = [0]
    for c in s:
        encoded.append(int(c))
    forbidden = 0
    ctrl_i = 1
    while ctrl_i < len(encoded):
        ctrl = 0
        for i in range(1, len(encoded)):
            if ctrl_i & i:
                ctrl ^= encoded[i]
        if not ctrl:
            forbidden |= ctrl_i
        ctrl_i = ctrl_i << 1
    encoded[forbidden] ^= 1
    decoded = []
    for i, c in enumerate(encoded):
        if i in POW2:
            continue
        decoded.append(str(c))
    return ''.join(decoded[1:])


def main():
    cmd = input()
    s = input().strip()
    if cmd == '1':
        print(encode(s))
    if cmd == '2':
        print(decode(s))


if __name__ == '__main__':
    main()
