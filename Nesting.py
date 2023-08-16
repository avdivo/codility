S = "(()(()()))"
def check(S):
    mem = 0
    for i in S:
        if i == '(':
            mem += 1
        else:
            mem -= 1
        if mem < 0:
            return 0
    return 1 if mem == 0 else 0

print(check(S))