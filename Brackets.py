S = "{[()()]}{{}}"
def buffer_check(buffer):
    buffer = []
    for i in range(len(S)):
        if S[i] in ['(', '{', '[']:
            buffer.append(S[i])
        else:
            if len(buffer) == 0:
                return 0
            if S[i] == ')' and buffer[-1] == '(':
                buffer.pop()
            elif S[i] == '}' and buffer[-1] == '{':
                buffer.pop()
            elif S[i] == ']' and buffer[-1] == '[':
                buffer.pop()
            else:
                return 0
    return 1 if len(buffer) == 0 else 0

print(buffer_check(S))
