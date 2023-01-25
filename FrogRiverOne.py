def solution(X, A):
    ok = set(range(1, X+1))
    for i, p in enumerate(A):
        ok -= {p}
        if not ok:
            return i
    return -1



print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

