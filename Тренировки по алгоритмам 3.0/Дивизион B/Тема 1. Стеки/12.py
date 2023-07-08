braces = {'}': '{', ']': '[', ')': '('}


def brace_sequence(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
            continue
        try:
            if stack.pop() != braces[c]:
                print('no')
                return
        except:
            print('no')
            return
    if len(stack):
        print('no')
    else:
        print('yes')

def main():
    brace_sequence(input())


if __name__ == '__main__':
    main()
