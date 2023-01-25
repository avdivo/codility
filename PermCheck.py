def solution(A):
    if len(set(A)) != len(A):
        return 0
    etalon = len(A) * (len(A) + 1) // 2
    if sum(A) == etalon:
        return 1
    return 0


print(solution([4, 1, 3]))

