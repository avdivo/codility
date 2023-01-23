def solution(A):
    best = diff = sc = t_sc = of = 0
    t = {'A': (5, 20), 'S': (40, 30)}
    for i in A:
        s, f = t[i]
        sc += s
        of += f
        diff += f - s
        if best < diff:
            best = diff
            of = 0
            t_sc = sc
    return t_sc + of

print(solution("ASAASS"))
