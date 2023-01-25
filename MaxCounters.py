from collections import Counter


def solution(N, A):
    stop = [i for i in range(len(A)) if A[i] > N]
    old = val = 0
    for s in stop:
        o = A[old:s]
        if o:
            val += max(Counter(o).values())
        old = s + 1
    c = [val] * N
    start = 0 if not stop else stop[-1] + 1
    for i in A[start:]:
        c[i-1] += 1
    return c

print(solution(5, [3, 4, 4, 6, 6, 1, 4, 4]))

